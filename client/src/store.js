import { compose, createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

// import { createLogger } from 'redux-logger';
// import { persistStore, autoRehydrate } from 'redux-persist';
import rootReducer from './reducers';

const store = createStore(
  rootReducer,
  compose(applyMiddleware(thunk)),
  // compose(applyMiddleware(createLogger()), autoRehydrate()),
  // compose(applyMiddleware(createLogger())),
);
// persistStore(store);
export default store;
