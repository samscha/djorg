import axios from 'axios';
import { login as login_auth } from '../util/auth';

axios.defaults.withCredentials = true;

// axios.defaults.xsrfHeaderName = 'X-CSRFToken'; /* for django */
// axios.defaults.xsrfCookieName = 'XCSRF-Token'; /* for django */

const appK = 'com.herokuapp.reactnotesapp-fwcdga47i';

export const AUTH_USER_AUTHENTICATED = 'AUTH_USER_AUTHENTICATED';
export const AUTH_USER_UNAUTHENTICATED = 'AUTH_USER_UNAUTHENTICATED';
export const AUTH_ERROR = 'AUTH_ERROR';
export const AUTH_CHECK = 'AUTH_CHECK';
export const AUTH_ERROR_RESET = 'AUTH_ERROR_RESET';

// signup
export const AUTH_SIGNUP_START = 'AUTH_SIGNUP_START';
export const AUTH_SIGNUP_SUCCESS = 'AUTH_SIGNUP_SUCCESS';
export const AUTH_SIGNUP_ERROR = 'AUTH_SIGNUP_ERROR';
export const AUTH_SIGNUP_FINISH = 'AUTH_SIGNUP_FINISH';

// login
export const AUTH_LOGIN_START = 'AUTH_LOGIN_START';
export const AUTH_LOGIN_SUCCESS = 'AUTH_LOGIN_SUCCESS';
export const AUTH_LOGIN_ERROR = 'AUTH_LOGIN_ERROR';
export const AUTH_LOGIN_FINISH = 'AUTH_LOGIN_FINISH';

// logout
export const AUTH_LOGOUT_START = 'AUTH_LOGOUT_START';
export const AUTH_LOGOUT_SUCCESS = 'AUTH_LOGOUT_SUCCESS';
export const AUTH_LOGOUT_ERROR = 'AUTH_LOGOUT_ERROR';
export const AUTH_LOGOUT_FINISH = 'AUTH_LOGOUT_FINISH';

// notes
export const NOTES_FETCH_START = 'NOTES_FETCH_START';
export const NOTES_FETCH_SUCCESS = 'NOTES_FETCH_SUCCESS';
export const NOTES_FETCH_ERROR = 'NOTES_FETCH_ERROR';
export const NOTES_FETCH_FINISH = 'NOTES_FETCH_FINISH';

export const NOTES_DELETE_START = 'NOTES_DELETE_START';
export const NOTES_DELETE_SUCCESS = 'NOTES_DELETE_SUCCESS';
export const NOTES_DELETE_FINISH = 'NOTES_DELETE_FINISH';

export const AUTH_NOTES_ERROR = 'AUTH_NOTES_ERROR';

// note
export const NOTE_EDIT_START = 'NOTE_EDIT_START';
export const NOTE_EDIT_SUCCESS = 'NOTE_EDIT_SUCCESS';
export const NOTE_EDIT_ERROR = 'NOTE_EDIT_ERROR';
export const NOTE_EDIT_FINISH = 'NOTE_EDIT_FINISH';

export const NOTE_DELETE_START = 'NOTE_DELETE_START';
export const NOTE_DELETE_SUCCESS = 'NOTE_DELETE_SUCCESS';
export const NOTE_DELETE_ERROR = 'NOTE_DELETE_ERROR';
export const NOTE_DELETE_FINISH = 'NOTE_ DELETE_FINISH';

export const NOTE_ADD_START = 'NOTE_ADD_START';
export const NOTE_ADD_SUCCESS = 'NOTE_ADD_SUCCESS';
export const NOTE_ADD_ERROR = 'NOTE_ADD_ERROR';
export const NOTE_ADD_FINISH = 'NOTE_ADDE_FINISH';

// const ROOT = 'https://reactnotesapp-fwcdga47i.herokuapp.com/api';
const ROOT = '127.0.0.1:8000/api';

export const resetErrors = _ => {
  return dispatch => {
    dispatch({ type: AUTH_ERROR_RESET });
  };
};

export const authenticateUser = _ => {
  return dispatch => {
    dispatch({ type: AUTH_LOGIN_START });

    axios
      .get(`${ROOT}/users/validate`, {
        headers: { authorization: localStorage.getItem(appK) },
      })
      .then(({ data }) => {
        dispatch({ type: AUTH_LOGIN_SUCCESS, payload: data.username });
        dispatch({ type: AUTH_LOGIN_FINISH });
      })
      .catch(err => {
        dispatch({ type: AUTH_LOGIN_ERROR, payload: err.response.data.error });
        dispatch({ type: AUTH_LOGIN_FINISH });
      });
  };
};

export const register = (username, password, confirmPassword, history) => {
  return dispatch => {
    dispatch({ type: AUTH_SIGNUP_START });

    if (!username || !password || !confirmPassword) {
      dispatch({
        type: AUTH_SIGNUP_ERROR,
        payload: 'Please provide all fields',
      });

      dispatch({ type: AUTH_SIGNUP_FINISH });
      return;
    }

    if (password !== confirmPassword) {
      dispatch({ type: AUTH_SIGNUP_ERROR, payload: 'Passwords do not match' });

      dispatch({ type: AUTH_SIGNUP_FINISH });
      return;
    }

    axios
      .post(`${ROOT}/users`, { username, password })
      .then(({ data }) => {
        dispatch({ type: AUTH_SIGNUP_SUCCESS, payload: data });

        dispatch({ type: AUTH_LOGIN_START });

        axios
          .post(`${ROOT}/users/login`, { username, password })
          .then(({ data }) => {
            localStorage.setItem(appK, data.token);

            dispatch({ type: AUTH_LOGIN_SUCCESS, payload: username });

            dispatch({ type: AUTH_LOGIN_FINISH });

            dispatch({ type: AUTH_SIGNUP_FINISH });

            history.push('/');
          })
          .catch(err => {
            dispatch({
              type: AUTH_LOGIN_ERROR,
              payload: err.response.data.message,
            });
            dispatch({ type: AUTH_LOGIN_FINISH });

            dispatch({ type: AUTH_SIGNUP_ERROR });
            dispatch({ type: AUTH_SIGNUP_FINISH });
          });
      })
      .catch(err => {
        dispatch({
          type: AUTH_SIGNUP_ERROR,
          payload: err.response.data.message,
        });
        dispatch({ type: AUTH_SIGNUP_FINISH });
      });
  };
};

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  console.log('cookie value', cookieValue);
  return cookieValue;
}

// function getCookie(name) {
//   if (!document.cookie) {
//     return null;
//   }

//   console.log('doc cooki', document.cookie);

//   const xsrfCookies = document.cookie
//     .split(';')
//     .map(c => c.trim())
//     .filter(c => c.startsWith(name + '='));

//   if (xsrfCookies.length === 0) {
//     return null;
//   }

//   return decodeURIComponent(xsrfCookies[0].split('=')[1]);
// }

export const login = (username, password, history) => {
  return dispatch => {
    dispatch({ type: AUTH_LOGIN_START });

    // axios({
    //   method: 'post',
    //   url: `http://127.0.0.1:8000/auth`,
    //   body: {
    //     username,
    //     password,
    //   },
    // })
    axios
      .post('http://127.0.0.1:8000/auth', { username, password })
      .then(function(response) {
        // store.dispatch(setToken(response.data.token))
        console.log(response.data);
        console.log(response.data.token);
        // localStorage.setItem(appK, response.data.token);
        dispatch({ type: AUTH_ERROR_RESET });

        dispatch({ type: AUTH_LOGIN_SUCCESS, payload: username });
        dispatch({ type: AUTH_LOGIN_FINISH });

        history.push('/');
      })
      .catch(function(error) {
        console.log(error);
        dispatch({
          type: AUTH_LOGIN_ERROR,
          payload: error.response.data.message,
        });
        dispatch({ type: AUTH_LOGIN_FINISH });
        // raise different exception if due to invalid credentials
        // if (_.get(error, 'response.status') === 400) {
        //   throw new InvalidCredentialsException(error);
        // }
        // throw error;
      });

    // console.log(getCookie('csrftoken'));

    // login_auth(username, password);

    // console.log('doc', document);

    // axios({
    //   method: 'post',
    //   url: `http://127.0.0.1:8000/auth`,
    //   body: {
    //     username,
    //     password,
    //   },
    //   // headers: {
    //   //   'X-CSRFToken': getCookie('csrftoken'),
    //   //   'X-Requested-With': 'XMLHttpRequest',
    //   //   'Content-Type': 'application/json',
    //   // },
    // })
    //   .then(({ data }) => {
    //     dispatch({ type: AUTH_ERROR_RESET });

    //     console.log('data', data);

    //     dispatch({ type: AUTH_LOGIN_SUCCESS, payload: username });
    //     dispatch({ type: AUTH_LOGIN_FINISH });

    //     history.push('/');
    //   })
    //   .catch(err => {
    //     dispatch({
    //       type: AUTH_LOGIN_ERROR,
    //       payload: err.response.data.message,
    //     });
    //     dispatch({ type: AUTH_LOGIN_FINISH });
    //   });

    // axios
    //   .post(`${ROOT}/users/login`, { username, password })
    //   .then(({ data }) => {
    //     dispatch({ type: AUTH_ERROR_RESET });

    //     localStorage.setItem(appK, data.token);

    //     dispatch({ type: AUTH_LOGIN_SUCCESS, payload: username });
    //     dispatch({ type: AUTH_LOGIN_FINISH });

    //     history.push('/');
    //   })
    //   .catch(err => {
    //     dispatch({
    //       type: AUTH_LOGIN_ERROR,
    //       payload: err.response.data.message,
    //     });
    //     dispatch({ type: AUTH_LOGIN_FINISH });
    //   });
  };
};

export const logout = history => {
  return dispatch => {
    dispatch({ type: AUTH_LOGOUT_START });

    localStorage.removeItem(appK);
    dispatch({ type: AUTH_LOGOUT_SUCCESS });

    dispatch({ type: AUTH_LOGOUT_FINISH });

    history.push('/login');
  };
};

// export const getNotes = _ => {
//   return dispatch => {
//     dispatch({ type: NOTES_FETCH_START });

//     axios
//       .get(`${ROOT}/users/notes`, {
//         headers: { authorization: localStorage.getItem(appK) },
//       })
//       .then(({ data }) => {
//         dispatch({ type: NOTES_FETCH_SUCCESS, payload: data });
//         dispatch({ type: NOTES_FETCH_FINISH });
//       })
//       .catch(err => {
//         dispatch({ type: AUTH_NOTES_ERROR, payload: err.response.data.error });
//         dispatch({ type: NOTES_FETCH_FINISH });
//       });
//   };
// };

export const getNotes = _ => {
  return dispatch => {
    dispatch({ type: NOTES_FETCH_START });

    axios
      .get(`/api/notes`)
      .then(({ data }) => {
        const notes = data.map(note => {
          const new_note = {};
          new_note._id = note.id;
          new_note.title = note.title;
          new_note.content = note.content;

          return new_note;
        });

        dispatch({ type: NOTES_FETCH_SUCCESS, payload: notes });
        dispatch({ type: NOTES_FETCH_FINISH });
      })
      .catch(err => {
        dispatch({ type: AUTH_NOTES_ERROR, payload: err.response.data.error });
        dispatch({ type: NOTES_FETCH_FINISH });
      });
  };
};

export const editNote = note => {
  return dispatch => {
    dispatch({ type: NOTE_EDIT_START });

    axios({
      method: 'PUT',
      url: `http://127.0.0.1:8000/api/notes/1/`,
      // data: {
      //   id: note.id,
      //   title: note.title,
      //   content: note.content,
      // },
      auth: {
        username: '#########################',
        password: '#####################',
      },
      headers: {
        // 'X-CSRFToken': getCookie('XCSRF-Token'),
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
      },
    })
      .then(({ data }) => {
        const note = { ...data, _id: data.id };
        delete note.id;

        dispatch({ type: NOTE_EDIT_SUCCESS, payload: note });
        dispatch({ type: NOTE_EDIT_FINISH });
      })
      .catch(err => {
        dispatch({ type: NOTE_EDIT_ERROR, payload: err });
        dispatch({ type: NOTE_EDIT_FINISH });
      });

    // axios
    //   .put(`${ROOT}/notes/${note.id}`, {
    //     title: note.title,
    //     content: note.content,
    //   })
    //   .then(({ data }) => {
    //     dispatch({ type: NOTE_EDIT_SUCCESS, payload: data });
    //     dispatch({ type: NOTE_EDIT_FINISH });
    //   })
    //   .catch(err => {
    //     dispatch({ type: NOTE_EDIT_ERROR, payload: err });
    //     dispatch({ type: NOTE_EDIT_FINISH });
    //   });
  };
};

// const getCookie = name => {
//   if (!document.cookie) {
//     return null;
//   }
//   const token = document.cookie
//     .split(';')
//     .map(c => c.trim())
//     .filter(c => c.startsWith(name + '='));

//   if (token.length === 0) {
//     return null;
//   }
//   return decodeURIComponent(token[0].split('=')[1]);
// };

// export const deleteNote = id => {
export const deleteNote = note => {
  return dispatch => {
    dispatch({ type: NOTE_DELETE_START });

    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/notes`,
      data: {
        id: note.id,
      },
      auth: {
        username: '#########################',
        password: '#####################',
      },
      // headers: {
      //   'X-CSRFToken': getCookie('csrfToken'),
      //   'X-Requested-With': 'XMLHttpRequest',
      //   'Content-Type': 'application/json',
      // },
    })
      .then(({ data }) => {
        dispatch({ type: NOTE_DELETE_SUCCESS, payload: data });
        dispatch({ type: NOTE_DELETE_FINISH });
      })
      .catch(err => {
        dispatch({ type: NOTE_DELETE_ERROR, payload: err });
        dispatch({ type: NOTE_DELETE_FINISH });
      });

    // axios
    //   .delete(`${ROOT}/notes/${id}`)
    //   .then(({ data }) => {
    //     dispatch({ type: NOTE_DELETE_SUCCESS, payload: data });
    //     dispatch({ type: NOTE_DELETE_FINISH });
    //   })
    //   .catch(err => {
    //     dispatch({ type: NOTE_DELETE_ERROR, payload: err });
    //     dispatch({ type: NOTE_DELETE_FINISH });
    //   });
  };
};

export const addNote = note => {
  return dispatch => {
    dispatch({ type: NOTE_ADD_START });
    // console.log(Cookie);

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/notes/`,
      data: {
        title: note.title,
        content: note.content,
      },
      auth: {
        username: 'admin',
        password: 'kokokoko',
      },
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      headers: {
        'X-CSRFToken': getCookie('X-CSRFToken'),
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json',
      },
    })
      .then(({ data }) => {
        const note = { ...data, _id: data.id };
        delete note.id;

        dispatch({ type: NOTE_ADD_SUCCESS, payload: note });
        dispatch({ type: NOTE_ADD_FINISH });
      })
      .catch(err => {
        dispatch({ type: NOTE_ADD_ERROR, payload: err });
        dispatch({ type: NOTE_ADD_FINISH });
      });

    // axios
    //   .post(`${ROOT}/notes`, note, {
    //     headers: { authorization: localStorage.getItem(appK) },
    //   })
    //   .then(({ data }) => {
    //     dispatch({ type: NOTE_ADD_SUCCESS, payload: data });
    //     dispatch({ type: NOTE_ADD_FINISH });
    //   })
    //   .catch(err => {
    //     dispatch({ type: NOTE_ADD_ERROR, payload: err });
    //     dispatch({ type: NOTE_ADD_FINISH });
    //   });
  };
};
