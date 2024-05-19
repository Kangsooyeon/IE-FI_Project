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

const searchBtnClicked = function () {
  if (specificRegion.value.province && specificRegion.value.city && specificRegion.value.region && bankValue.value) {
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
    }};

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