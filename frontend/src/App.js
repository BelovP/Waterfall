import React, {Component, Image, View} from 'react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import request from 'superagent'
import MainComponent from './components/MainComponent'
import $ from 'jquery'
import jQuery from 'jquery'
//import anno from './components/annotorious/annotorious.min.js'
//var __html = require('annotorious/example/example.html');
//var template = { __html: __html };

class App extends Component {
  constructor(props, context) {
    super(props, context);
    this.state = {}
    this.state.annotations_loaded = false;
    this.state.record_id = 2;
  }

  componentDidMount() {
    console.log(this.state.annotations_loaded);
    if (this.state.annotations_loaded == false) {
      anno.reset();
      $.ajax({
        type: "GET",
        url: 'http://localhost:8000/api/v1/annotations/',
        data: {record: this.state.record_id},
        dataType: 'json',
        cache: false,
        success: function(data) {
          for (var i = 0; i < data.results.length; ++i) {
            var result = data.results[i];
            console.log('annotation added');
            debugger;
            var myAnnotation = {
                src: "http://localhost:8080/my-dummy-image-path",
                text : result.label,
                shapes : [{
                    type : 'rect',
                    geometry : { x : result.x1, y: result.t1, width : result.x2 - result.x1, height: result.t2 - result.t1 }
                }]
            };
            anno.addAnnotation(myAnnotation);
            console.log('annotation added');
          }
          //this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error('error', status, err.toString());
        }.bind(this)
      });
      this.state.annotations_loaded = true;
    }
  }

  render() {
    jQuery.noConflict();
    anno.addHandler('onAnnotationCreated', function(annotation) {
      console.log('new annotation');
      var x1_val = annotation.shapes[0].geometry.x;
      var x2_val = annotation.shapes[0].geometry.x + annotation.shapes[0].geometry.width;
      var t1_val = annotation.shapes[0].geometry.y;
      var t2_val = annotation.shapes[0].geometry.y + annotation.shapes[0].geometry.height;
      var record_id = 2;
      $.ajax({
        type: "POST",
        url: 'http://localhost:8000/api/v1/annotations/',
        data: {t1: t1_val, t2: t2_val, x1: x1_val, x2: x2_val, label: annotation.text, record: record_id},
        dataType: 'json',
        cache: false,
        success: function(data) {
          console.log('successful request');
          //this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error('error', status, err.toString());
        }.bind(this)
      });
    });

    anno.addHandler('onAnnotationRemoved', function(annotation) {
      console.log('removed annotation');
      var x1_val = annotation.shapes[0].geometry.x;
      var x2_val = annotation.shapes[0].geometry.x + annotation.shapes[0].geometry.width;
      var t1_val = annotation.shapes[0].geometry.y;
      var t2_val = annotation.shapes[0].geometry.y + annotation.shapes[0].geometry.height;
      var record_id = 2;
      $.ajax({
        type: "DELETE",
        url: 'http://localhost:8000/api/v1/annotations/',
        data: {t1: t1_val, t2: t2_val, x1: x1_val, x2: x2_val, label: annotation.text, record: record_id},
        dataType: 'json',
        cache: false,
        success: function(data) {
          console.log('successful delete');
          //this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
          console.error('error', status, err.toString());
        }.bind(this)
      });
    });
    return (
      <div>
        <img src="images/waterfall.png" className="annotatable" data-original="http://localhost:8080/my-dummy-image-path"/>
      </div>
    )
    return (
      <div>
        <MainComponent text={'Hello, REACT!!'}/>
      </div>
    )
  }
}

export default App
