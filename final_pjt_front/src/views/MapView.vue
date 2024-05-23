<template>
  <div class="container mt-0">
    <h1 class="my-4 title">가까운 은행 찾기</h1>
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

    <div class="text-center d-flex flex-row justify-content-end">
      <button @click="searchBtnClicked" class="btn btn-primary">검색</button>
      <button @click="resetLocation" class="btn btn-secondary ml-2">초기 위치로 이동</button>
    </div>

    <div class="row mt-4">
      <div class="mb-3">
        <div id="map" style="width: 100%; height: 400px"></div>
      </div>
      <div class="list-container" :class="{'visible-list': isNotList}">
        <ul id="placesList" class="list-group list-scroll"></ul>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useProjectStore } from '@/stores/project';
import SelectRegion from '@/components/utils/SelectRegion.vue';

const store = useProjectStore();
const KAKAO_MAP_API_KEY = import.meta.env.VITE_ENV_KAKAO_MAP_API_KEY;

const cityList = ref([]);
const regionList = ref([]);
const specificRegion = ref({});
const markers = ref([]);
const isNotList = ref(true);
const map = ref(null); // map 객체를 저장할 ref 추가

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

const bankValue = ref(''); // 은행 선택을 위한 변수 선언
const bnakSeleted = function (event) { // 은행 선택을 위한 함수 선언
  bankValue.value = event.target.value;
}

var infowindow = '';

const searchBtnClicked = function () {
  isNotList.value = false;
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
    map.value.setCenter(new kakao.maps.LatLng(resultLocation.latitude, resultLocation.longitude));

    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    var ps = new kakao.maps.services.Places();

    // 키워드로 장소를 검색합니다
    ps.keywordSearch(`${specificRegion.value.province} ${specificRegion.value.city} ${specificRegion.value.region} ${bankValue.value}`, (data, status, pagination) => {
      placesSearchCB(data, status, pagination);
    });
  }
};

let defaultLocation = { latitude: 37.566826, longitude: 126.9786567 }; // 기본 위치: 서울

const resetLocation = function () {
  map.value.setCenter(new kakao.maps.LatLng(defaultLocation.latitude, defaultLocation.longitude));
};

function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    var bounds = new kakao.maps.LatLngBounds();
    markers.value = [];

    for (var i = 0; i < data.length; i++) {
      const marker = displayMarker(data[i], i);
      markers.value.push(marker);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    map.value.setBounds(bounds);

    displayPlaces(data); // 검색 결과 목록을 업데이트합니다
  }
}

function displayMarker(place, index) {
  var marker = new kakao.maps.Marker({
    map: map.value,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  kakao.maps.event.addListener(marker, 'click', function () {
    infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
    infowindow.open(map.value, marker);
    highlightList(index);
  });

  return marker;
}

// 검색 결과 목록을 업데이트하는 함수입니다
function displayPlaces(places) {
  var listEl = document.getElementById('placesList');
  var fragment = document.createDocumentFragment();

  // 기존에 추가된 항목들을 제거합니다
  removeAllChildNods(listEl);

  for (var i = 0; i < places.length; i++) {
    var itemEl = getListItem(i, places[i]);
    fragment.appendChild(itemEl);
  }

  listEl.appendChild(fragment);
}

// 검색결과 항목을 Element로 반환하는 함수입니다
function getListItem(index, place) {
  var el = document.createElement('li'),
      itemStr = '<span class="markerbg marker_' + (index + 1) + '"></span>' +
                '<div class="info">' +
                '   <h5>' + place.place_name + '</h5>';

  if (place.road_address_name) {
      itemStr += '    <span>' + place.road_address_name + '</span>' +
                  '   <span class="jibun gray">' +  place.address_name  + '</span>';
  } else {
      itemStr += '    <span>' +  place.address_name  + '</span>'; 
  }

  itemStr += '  <span class="tel">' + place.phone  + '</span>' +
            '</div>';           

  el.innerHTML = itemStr;
  el.className = 'list-group-item small'; // list-group-item 및 작은 글자 크기 적용
  el.onclick = function() {
    map.value.setCenter(new kakao.maps.LatLng(place.y, place.x)); // 마커 위치로 지도 중심 이동
    kakao.maps.event.trigger(markers.value[index], 'click');
  };

  return el;
}

// 검색결과 목록의 자식 Element를 제거하는 함수입니다
function removeAllChildNods(el) {   
  while (el.hasChildNodes()) {
    el.removeChild(el.lastChild);
  }
}

function highlightList(index) {
  const items = document.querySelectorAll('#placesList .list-group-item');
  items.forEach((item, idx) => {
    if (idx === index) {
      item.style.backgroundColor = '#e3f2fd';
    } else {
      item.style.backgroundColor = '';
    }
  });
}

const setLocation = function (latitude, longitude) {
  const container = document.getElementById('map');
  const options = {
    center: new kakao.maps.LatLng(latitude, longitude),
    level: 3,
  };
  map.value = new kakao.maps.Map(container, options);
};

const getCurrentLocation = () => {
  return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        resolve(position.coords);
      }, err => {
        reject(err);
      });
    } else {
      reject(new Error('Geolocation not supported'));
    }
  });
};

onMounted(async () => {
  const apiKey = KAKAO_MAP_API_KEY; // 여기서 YOUR_KAKAO_API_KEY를 실제 API 키로 대체하세요

  loadKakaoMaps(apiKey, async () => {
    // Kakao Maps API 로드 완료 후 실행할 코드
    kakao.maps.load(async () => {
      try {
        const coords = await getCurrentLocation();
        defaultLocation = { latitude: coords.latitude, longitude: coords.longitude };
        setLocation(coords.latitude, coords.longitude);
      } catch (error) {
        console.error(error);
        setLocation(defaultLocation.latitude, defaultLocation.longitude); // 기본 위치: 서울
      }
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
.container {
  width: 960px;
  height: 1100px;
  text-align: left;
  border: 1px solid #e9ecef;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
}
.list-container {
  height: 380px; /* 지도와 동일한 높이로 설정 */
  overflow-y: scroll; /* 스크롤 가능하게 설정 */
}
.small {
  font-size: 0.875rem; /* 글자 크기 작게 설정 */
}
.visible-list {
  display: none;
}
</style>

