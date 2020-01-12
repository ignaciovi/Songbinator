import React from 'react';
import Cookies from 'js-cookie';
import './App.css';
import 'bulma/css/bulma.css'
import { Login } from './Login';
import { AppComponent } from './AppComponent';
import ReactGA from 'react-ga';
import { createBrowserHistory } from 'history'


// ReactGA.initialize('UA-156008572-1')
// const browserHistory = createBrowserHistory()
// browserHistory.listen((location:any, action:any) => {
//   ReactGA.pageview(location.pathname + location.search)
// })

ReactGA.initialize('UA-156008572-1');

export default class App extends React.Component {

  render() {
    const logged = Cookies.get('spotify_code') === undefined ? false : true;

    ReactGA.pageview(window.location.pathname + window.location.search)
    
    return (
      <div className="App">
        {!logged ?
          <Login />
          : 
          <AppComponent />
        }
      </div>
    );
  }
}

