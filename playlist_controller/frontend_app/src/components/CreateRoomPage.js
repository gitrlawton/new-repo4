import React, { Component } from 'react';
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import { Link } from "react-router-dom";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";

export default class CreateRoomPage extends Component {
    // Value for the default amount of votes to show.
    defaultVotes = 2;

    constructor(props) {
        super(props);
    }

    render() {
        return <Grid container spacing={1}>
            {/* This first Grid item is a text header. */}
            <Grid item xs={12} align="center">
                <Typography component="h4" variant="h4">
                    Create A Room
                </Typography>
            </Grid>
            {/* This Grid item is a text header with two radio buttons */}
            {/* to control whether user can control playback */}
            <Grid item xs={12} align="center">
                <FormControl component="fieldset">
                    {/* Text header for radio group. */}
                    <FormHelperText>
                        <div align="center">
                            Guest Control of Playback State
                        </div>
                    </FormHelperText>
                    {/* Radio button group. */}
                    <RadioGroup row defaultValue="true">
                        {/* Label for radio button with label "Play/Pause". */}
                        <FormControlLabel 
                            value="true" control={<Radio color="primary" />}
                            label="Play/Pause" labelPlacement="bottom"
                        />
                        {/* Label for radio button with label "No Control". */}
                        <FormControlLabel 
                            value="false" control={<Radio color="secondary" />}
                            label="No Control" labelPlacement="bottom"
                        />
                    </RadioGroup>
                </FormControl>
            </Grid>
        </Grid>;
    }
}