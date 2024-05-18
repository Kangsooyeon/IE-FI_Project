<template>
  <div>
    <div>
      <SelectRegion
        :changed="provinceChanged"
        :region-list="store.provinceList"
        title="시/도"
      />

      <SelectRegion
        :changed="cityChanged"
        :region-list="cityList"
        title="시/군/구"
      />

      <SelectRegion
        :changed="regionChanged"
        :region-list="regionList"
        title="읍/면/동"
      />
    </div>

    <button @click="searchBtnClicked">검색</button>

    <div id="map" style="width: 500px; height: 400px"></div>
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

const searchBtnClicked = function () {
  store.regionList.find((el) => {
    if (
      el.province === specificRegion.value.province &&
      el.city === specificRegion.value.city &&
      el.region === specificRegion.value.region
    ) {
      console.log(el.latitude, el.longitude);
      // 1.여기서 지도에 위치로 이동하는 함수를 작성하시오
      const map = setLocation(el.latitude, el.longitude);
      // 2.여기에 마커 관련함수 작성
    }
  });
};

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
  script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${apiKey}`;
  document.head.appendChild(script);
}
</script>

<style scoped></style>
