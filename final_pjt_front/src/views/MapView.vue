<template>
  <div>
    <div id="map"></div>
    <div class="button-group">
      <select v-model="selectedRegion">
        <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
      </select>
      <select v-model="selectedBank">
        <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
      </select>
      <button @click="searchBank">Search Bank</button>
      <button @click="changeSize(0)">Hide</button>
      <button @click="changeSize(400)">Show</button>
      <button @click="displayMarker(markerPositions1)">Marker Set 1</button>
      <button @click="displayMarker(markerPositions2)">Marker Set 2</button>
      <button @click="displayMarker([])">Marker Set 3 (Empty)</button>
      <button @click="displayInfoWindow">Info Window</button>
    </div>
  </div>
</template>

<script>
import { ref, toRaw, reactive } from "vue";
import axios from "axios";

export default {
  name: "KakaoMap",
  data() {
    return {
      regions: ["Seoul", "Busan", "Incheon"],
      banks: ["Hana Bank", "Shinhan Bank", "Kookmin Bank"],
      selectedRegion: "Seoul",
      selectedBank: "Hana Bank",
      markerPositions1: [
        [33.452278, 126.567803],
        [33.452671, 126.574792],
        [33.451744, 126.572441],
      ],
      markerPositions2: [
        [37.499590490909185, 127.0263723554437],
        [37.499427948430814, 127.02794423197847],
        [37.498553760499505, 127.02882598822454],
        [37.497625593121384, 127.02935713582038],
        [37.49629291770947, 127.02587362608637],
        [37.49754540521486, 127.02546694890695],
        [37.49646391248451, 127.02675574250912],
      ],
      markers: [],
      infowindow: null,
      map: null,
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=b1ff86fb67ad26971d65aaa9a29e6eca";
      document.head.appendChild(script);
    }
  },
  methods: {
    initMap() {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 5,
      };

      this.map = new kakao.maps.Map(container, options);
    },
    changeSize(size) {
      const container = document.getElementById("map");
      container.style.width = `${size}px`;
      container.style.height = `${size}px`;
      toRaw(this.map).relayout();
    },
    displayMarker(markerPositions) {
      if (this.markers.length > 0) {
        this.markers.forEach((marker) => marker.setMap(null));
      }

      const positions = markerPositions.map(
        (position) => new kakao.maps.LatLng(...position)
      );

      if (positions.length > 0) {
        this.markers = positions.map(
          (position) =>
            new kakao.maps.Marker({
              map: toRaw(this.map),
              position,
            })
        );

        const bounds = positions.reduce(
          (bounds, latlng) => bounds.extend(latlng),
          new kakao.maps.LatLngBounds()
        );

        toRaw(this.map).setBounds(bounds);
      }
    },
    displayInfoWindow() {
      if (this.infowindow && this.infowindow.getMap()) {
        toRaw(this.map).setCenter(this.infowindow.getPosition());
        return;
      }

      var iwContent = '<div style="padding:5px;">Hello World!</div>', 
        iwPosition = new kakao.maps.LatLng(33.450701, 126.570667), 
        iwRemoveable = true;

      this.infowindow = new kakao.maps.InfoWindow({
        map: toRaw(this.map),
        position: iwPosition,
        content: iwContent,
        removable: iwRemoveable,
      });

      toRaw(this.map).setCenter(iwPosition);
    },
    async searchBank() {
      try {
        const response = await axios.get(`https://dapi.kakao.com/v2/local/search/keyword.json`, {
          headers: { Authorization: `KakaoAK b1ff86fb67ad26971d65aaa9a29e6eca` },
          params: {
            query: this.selectedBank,
            category_group_code: 'BK9',
            x: this.map.getCenter().getLng(),
            y: this.map.getCenter().getLat(),
            radius: 5000
          }
        });
        const { documents } = response.data;
        const positions = documents.map(
          doc => [parseFloat(doc.y), parseFloat(doc.x)]
        );
        this.displayMarker(positions);
      } catch (error) {
        console.error(error);
      }
    }
  },
};
</script>

<style scoped>
#map {
  width: 400px;
  height: 400px;
}

.button-group {
  margin: 10px 0px;
}

button {
  margin: 0 3px;
}
</style>
