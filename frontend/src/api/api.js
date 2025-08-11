import axios from "axios";

/* This is a bad practice... */
const API_BASE_URL = 'http://127.0.0.1:8000/api';

async function callApiGet(method, params = null) {
  try{
    let queryUrl = `${API_BASE_URL}/${method}/`;
    if (params !== null) {
      queryUrl += `${params}`;
    }
    return await axios.get(queryUrl);
  } catch (error) {
    console.log(error);
  }
}

export async function GetRetailers(params) {
  if (params !== null && params !== 'All') {
    return await callApiGet(`retailers`, params);
  }
  return await callApiGet(`retailers`);
}

export async function GetCoupons(params) {
  if (params !== null && params !== 'All') {
    return await callApiGet(`coupons`, params);
  }
  return await callApiGet(`coupons`);
}

export async function GetStatistics(params) {
  if (params !== null && params !== 'All') {
    return await callApiGet(`statistics`, params);
  }
  return await callApiGet(`statistics`);
}
