import { TOKEN_SET } from '../actions';
// import { INITIALIZE } from 'redux-form/lib/actionTypes';
// import { actionTypes } from 'redux-form';

const initialState = [];
export default (state = initialState, action) => {
  switch (action.type) {
    case TOKEN_SET:
      return action.data;

    default:
      return state;
  }
};

// export default (notes = initialState, action) => {
//   switch (action.type) {
//     case NOTES_FETCH_SUCCESS:
//       return action.payload;

//     // case NOTES_FETCH_ERROR:
//     case NOTE_EDIT_SUCCESS:
//       return notes.map(
//         note => (note._id === action.payload._id ? action.payload : note),
//       );

//     case NOTE_DELETE_SUCCESS:
//       return notes.filter(note => note._id !== action.payload._id);

//     case NOTE_ADD_SUCCESS:
//       return [...notes, action.payload];

//     case AUTH_LOGOUT_SUCCESS:
//       return [];

//     default:
//       return notes;
//   }
// };
