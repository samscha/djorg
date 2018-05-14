import React, { Component } from 'react';
import { connect } from 'react-redux';

import { authenticateUser } from '../../actions';

const appK = 'com.herokuapp.reactnotesapp-fwcdga47i';

export default ComposedComponent => {
  class CheckAuthentication extends Component {
    componentWillMount() {
      if (!localStorage.getItem(appK)) {
        // window.alert('Please log in first');
        this.props.history.push('/login');
      }

      if (!this.props.user) {
        this.props.authenticateUser();
      }
    }

    render() {
      return (
        <div className="CheckAuthentication">
          {localStorage.getItem(appK) ? (
            <ComposedComponent history={this.props.history} />
          ) : null}
        </div>
      );
    }
  }

  const mapStateToProps = state => {
    return {
      user: state.auth.user,
    };
  };

  return connect(mapStateToProps, { authenticateUser })(CheckAuthentication);
};
