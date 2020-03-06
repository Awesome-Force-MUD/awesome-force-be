## Team Awesome Force MUD Application



### Meet the Team

> Back End Dango Engineers
>
> - Ben Griffin
> - Jason Murphy
> - Navo Visagan
>
> Front End Engineers
>
> - Angela Flowers
> - Kristin Barr

### Why a MUD Application?

> This application was designed to test our Python knowledge along with our problem solving skills. We as a team took on the task of learning Django a RESTful back end framework designed for Python driven applications. 

 ### Our Application

> A simple MUD that allows registered players to login and navigate through over 150 rooms.
>
> Each room is connected to at least one room that we designed to randomly create in a zig-zag fashion.
>
> Registered players will start in the middle of the map and begin moving their way out of the map using the directions North, South, East, West.

------

## Endpoints

### Room Data returned in JSON

> ```json
> [    
>         {
>         "title": "Outside Cave Entrance",
>         "description": "North of you, the cave mount beckons",
>         "n_to": 496,
>         "s_to": -1,
>         "e_to": -1,
>         "w_to": -1,
>         "loc_x": 127,
>         "loc_y": 20
>     },
>     {
>         "title": "Foyer",
>         "description": "Dim light filters in from the south. Dusty\npassages run north and east.",
>         "n_to": 497,
>         "s_to": 495,
>         "e_to": 1124,
>         "w_to": 1126,
>         "loc_x": 128,
>         "loc_y": 20
>     },
>  ]
> ```

### Player Endpoints

> ```json
> [
>     {
>         "player_name": "navos Player",
>         "players_current_room": 42
>     },
>     {
>         "player_name": "bens player",
>         "players_current_room": 42
>     },
>     {
>         "player_name": "freds player",
>         "players_current_room": 42
>     }
> ]
> ```