import React, {Component} from 'react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import request from 'superagent'
import MainComponent from './components/MainComponent'


class App extends Component {
  constructor(props, context) {
    super(props, context);
    this.state = {}
  }

  render() {
    return (
      <MuiThemeProvider>
        <MainComponent text={'Hello, REACT'}/>
      </MuiThemeProvider>
    )
  }
}

export default App
