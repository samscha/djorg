import axios from 'axios';
import store from '../store';
// import { URL } from '../config/Api';
const URL = 'http://127.0.0.1:8000/';

export const apiClient = function() {
  const token = store.getState().token;
  const params = {
    baseURL: URL,
    headers: { Authorization: 'Token ' + token },
  };
  return axios.create(params);
};
