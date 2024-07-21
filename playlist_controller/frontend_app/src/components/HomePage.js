import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

export default class HomePage extends Component {
    constructor(props) {
      super(props);
    }

    render() {
        return (
            // The Router will redirect us to the correct page.
            // The Switch will allow us to switch on the path name (like a
            // switch statement.)
            // The Routes are the cases in that switch statement.
            // If the address typed into the url bar matches one of the paths,
            // the contents of that route will be rendered.
            // In the example below, the first path will simply render a <p> tag
            // if the path '/' is visited.
            // If the path '/join' is visited, the RoomJoinPage component will
            // be rendered, and so on.
            // 
            // Note: after passing paths to the routes, as done below, you must
            // then go to the urls.py file inside the frontend_app directory
            // and add those same paths to the urlpatterns list.
            //
            // Note: the exact keyword is needed for the path if you want to
            // adhere to strict matching of urls.  Without exact, every url
            // that begins with a '/' will be matched to the first path, thus 
            // rendering the home page for any and all urls, even if '/join' or
            // '/create' is actually visited.
            <Router>
                <Switch>
                    <Route exact path="/">
                        <p>This is the home page</p>
                    </Route>
                    <Route path="/join" component={RoomJoinPage} />
                    <Route path="/create" component={CreateRoomPage} />
                </Switch>
            </Router>
        );
      }
    }