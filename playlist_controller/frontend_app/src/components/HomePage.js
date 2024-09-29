import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import Room from "./Room";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      roomCode: null,
    };
    this.clearRoomCode = this.clearRoomCode.bind(this);
  }

  // Lifecycle method.
  async componentDidMount() {
    // Send a GET request to the '/api/user-in-room' endpoint.
    fetch("/api/user-in-room")
      .then((response) => response.json()) // When the server responds, convert the response to a JSON object
      .then((data) => {
        // Refer to the JSON object (response) as "data" and...
        // Update the component's state with the room code retrieved from the response.
        this.setState({
          roomCode: data.code,
        });
      });
  }

  // JSX to be displayed when we visit the "/" endpoint.
  renderHomePage() {
    return (
      <Grid container spacing={3}>
        <Grid item xs={12} align="center">
          <Typography variant="h3" compact="h3">
            House Party
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <ButtonGroup disableElevation variant="contained" color="primary">
            <Button color="primary" to="/join" component={Link}>
              Join a Room
            </Button>
            <Button color="secondary" to="/create" component={Link}>
              Create a Room
            </Button>
          </ButtonGroup>
        </Grid>
      </Grid>
    );
  }

  clearRoomCode() {
    // Reset our state.
    this.setState({
      roomCode: null,
    });
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
          <Route
            exact
            path="/"
            render={() => {
              return this.state.roomCode ? (
                <Redirect to={`/room/${this.state.roomCode}`} />
              ) : (
                this.renderHomePage()
              );
            }}
          />
          <Route path="/join" component={RoomJoinPage} />
          <Route path="/create" component={CreateRoomPage} />
          {/* The semi-colon denotes a placeholder variable. */}
          <Route
            path="/room/:roomCode"
            render={(props) => {
              return <Room {...props} leaveRoomCallback={this.clearRoomCode} />;
            }}
          />
        </Switch>
      </Router>
    );
  }
}
