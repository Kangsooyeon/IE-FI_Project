<template>
  <div class="container mt-4">
    <h1 class="mb-4 title">가까운 은행 찾기</h1>
    <div class="row mb-3">
      <div class="col-md-3">
        <SelectRegion
          :changed="provinceChanged"
          :region-list="store.provinceList"
          title="시/도"
          class="form-select"
        />
      </div>

      <div class="col-md-3">
        <SelectRegion
          :changed="cityChanged"
          :region-list="cityList"
          title="시/군/구"
          class="form-select"
        />
      </div>

      <div class="col-md-3">
        <SelectRegion
          :changed="regionChanged"
          :region-list="regionList"
          title="읍/면/동"
          class="form-select"
        />
      </div>

      <div class="col-md-3">
        <SelectRegion
          :changed="bnakSeleted"
          :region-list="store.koreanBanks"
          title="은행선택"
          class="form-select"
        />
      </div>
    </div>

    <div class="text-center d-flex">
      <button @click="searchBtnClicked" class="btn btn-primary">검색</button>
    </div>

    <div id="map" class="mt-4" style="width: 100%; height: 400px"></div>
  </div>
</template>


<script setup>
import SelectRegion from '@/components/utils/SelectRegion.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useProjectStore } from '@/stores/project';

const store = useProjectStore();

const KAKAO_MAP_API_KEY = import.meta.env.VITE_ENV_KAKAO_MAP_API_KEY;

const cityList = ref([]);
const regionList = ref([]);
const specificRegion = ref({});

const provinceChanged = function (event) {
  regionList.value = [];
  cityList.value = store.getCityList(event.target.value);
  specificRegion.value.province = event.target.value;
};

const cityChanged = function (event) {
  regionList.value = store.getSpecificRegionList(
    specificRegion.value.province,
    event.target.value
  );
  specificRegion.value.city = event.target.value;
};

const regionChanged = function (event) {
  specificRegion.value.region = event.target.value;
};

const bankValue= ref(''); // 1.은행선택을 위한 변수 선언
const bnakSeleted = function(event) { // 2.은행선택을 위한 함수 선언
  bankValue.value = event.target.value;
}

var infowindow = ''

const searchBtnClicked = function () {
  if (specificRegion.value.province && specificRegion.value.city && specificRegion.value.region && bankValue.value) {
    const resultLocation = store.regionList.find((el) => {
      if (
        el.province === specificRegion.value.province &&
        el.city === specificRegion.value.city &&
        el.region === specificRegion.value.region
      ) {
        return el;
      }
    });
    console.log(resultLocation);
    console.log(resultLocation.latitude, resultLocation.longitude);
    const map = setLocation(resultLocation.latitude, resultLocation.longitude);

     infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    var ps = new kakao.maps.services.Places();

    // 키워드로 장소를 검색합니다
    ps.keywordSearch(`${specificRegion.value.province} ${specificRegion.value.city} ${specificRegion.value.region} ${bankValue.value}`, (data, status, pagination) => {
      placesSearchCB(data, status, pagination, map);
    });
  }
};

function placesSearchCB(data, status, pagination, map) {
  if (status === kakao.maps.services.Status.OK) {
    var bounds = new kakao.maps.LatLngBounds();

    for (var i = 0; i < data.length; i++) {
      displayMarker(data[i], map);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    map.setBounds(bounds);
  }
}

function displayMarker(place, map) {
  var marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  kakao.maps.event.addListener(marker, 'click', function () {
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
    infowindow.open(map, marker);
  });
}

const setLocation = function (latitude = 33.450701, longitude = 126.570667) {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(latitude, longitude),
    level: 3,
  };
  const map = new kakao.maps.Map(container, options);
  return map;
};

onMounted(() => {
  const apiKey = KAKAO_MAP_API_KEY; // 여기서 YOUR_KAKAO_API_KEY를 실제 API 키로 대체하세요

  loadKakaoMaps(apiKey, () => {
    // Kakao Maps API 로드 완료 후 실행할 코드
    kakao.maps.load(() => {
      setLocation();
    });
  });
});

function loadKakaoMaps(apiKey, callback) {
  const script = document.createElement('script');
  script.onload = () => callback();
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}&libraries=services,clusterer,drawing`;
  document.head.appendChild(script);
}
</script>

<style scoped>
.title {
  font-size: 2rem;
  font-weight: 600;
  margin-left: auto;
}
.container{
  width:960px;
  text-align:left;
}
</style>