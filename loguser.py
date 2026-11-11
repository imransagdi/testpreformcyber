def build_log_page(room):

    game = room["game"]

    players = list(
        game.players.values()
    )

    player_cards = []

    for player in players:

        player_cards.append(
            f"""
            <section class="player-card">

                <div class="player-header">

                    <div class="player-name">
                        {player.name}
                    </div>

                    <div class="player-ip">
                        IP: {player.ip}
                    </div>

                </div>


                <div class="stats">

                    <div class="stat">

                        <div class="label">
                            COINS
                        </div>

                        <div class="value">
                            {player.economy.coins}
                        </div>

                    </div>


                    <div class="stat">

                        <div class="label">
                            HACKS DONE
                        </div>

                        <div class="value">
                            {getattr(
                                player,
                                "hacks_done",
                                0
                            )}
                        </div>

                    </div>

                </div>

            </section>
            """
        )

    if not player_cards:

        player_cards.append(
            """
            <div class="empty">
                NO PLAYERS IN ROOM
            </div>
            """
        )

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<meta
    http-equiv="Cache-Control"
    content="no-cache, no-store, must-revalidate"
>

<meta
    http-equiv="Pragma"
    content="no-cache"
>

<meta
    http-equiv="Expires"
    content="0"
>

<title>CYBER//NET USER LOG</title>

<style>

* {{
    box-sizing: border-box;
}}

html,
body {{
    margin: 0;
    padding: 0;
}}

body {{

    background: #050605;

    color: #c8c8c8;

    font-family:
        Consolas,
        "Courier New",
        monospace;

    padding: 18px;

    min-height: 100vh;
}}


/* =====================================================
   HEADER
   ===================================================== */

.header {{

    max-width: 1000px;

    margin:
        0 auto 18px;

    padding: 18px;

    background: #090b09;

    border:
        1px solid #303530;
}}

.title {{

    color: #8cff8c;

    font-size: 24px;

    font-weight: bold;

    letter-spacing: 1px;
}}

.subtitle {{

    margin-top: 6px;

    color: #666;

    font-size: 11px;
}}

.room-info {{

    margin-top: 12px;

    color: #888;

    font-size: 12px;
}}

.room-code {{

    color: white;

    font-weight: bold;
}}


/* =====================================================
   PLAYER GRID
   ===================================================== */

.players {{

    max-width: 1000px;

    margin: 0 auto;

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(
                280px,
                1fr
            )
        );

    gap: 14px;
}}


/* =====================================================
   PLAYER CARD
   ===================================================== */

.player-card {{

    background: #090b09;

    border:
        1px solid #303530;
}}


.player-header {{

    padding: 16px;

    border-bottom:
        1px solid #303530;
}}


.player-name {{

    color: #9cff9c;

    font-size: 20px;

    font-weight: bold;

    overflow-wrap: anywhere;
}}


.player-ip {{

    margin-top: 6px;

    color: #666;

    font-size: 12px;

    overflow-wrap: anywhere;
}}


/* =====================================================
   STATS
   ===================================================== */

.stats {{

    display: grid;

    grid-template-columns:
        1fr 1fr;
}}


.stat {{

    padding: 18px;

    text-align: center;

    border-right:
        1px solid #303530;
}}


.stat:last-child {{

    border-right: 0;
}}


.label {{

    color: #666;

    font-size: 11px;

    margin-bottom: 8px;
}}


.value {{

    color: #ddd;

    font-size: 26px;

    font-weight: bold;
}}


/* =====================================================
   EMPTY
   ===================================================== */

.empty {{

    grid-column: 1 / -1;

    padding: 30px;

    text-align: center;

    color: #555;

    background: #090b09;

    border:
        1px solid #303530;
}}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {{

    max-width: 1000px;

    margin:
        18px auto 0;

    color: #444;

    font-size: 10px;

    text-align: center;
}}


/* =====================================================
   MOBILE
   ===================================================== */

@media (
    max-width: 600px
) {{

    body {{
        padding: 10px;
    }}

    .header {{
        padding: 14px;
    }}

    .title {{
        font-size: 20px;
    }}

    .players {{
        grid-template-columns:
            1fr;
    }}

    .player-name {{
        font-size: 18px;
    }}

    .value {{
        font-size: 23px;
    }}

}}

</style>

</head>


<body>


<div class="header">

    <div class="title">
        CYBER//NET USER LOG
    </div>

    <div class="subtitle">
        ALL PLAYERS IN CURRENT ROOM
    </div>

    <div class="room-info">

        ROOM:

        <span class="room-code">
            {room.get("code", "UNKNOWN")}
        </span>

        &nbsp; | &nbsp;

        PLAYERS:
        {len(players)}

    </div>

</div>


<div class="players">

    {"".join(player_cards)}

</div>


<div class="footer">

    CYBER//NET

</div>


<script>

/* =====================================================
   LIVE USER LOG UPDATE
   ===================================================== */

let updating = false;


async function updateUserLog() {{

    if (updating) {{
        return;
    }}

    updating = true;

    try {{

        const response = await fetch(
            window.location.href,
            {{
                method: "GET",

                cache: "no-store",

                headers: {{
                    "Cache-Control":
                        "no-cache, no-store, must-revalidate",

                    "Pragma":
                        "no-cache"
                }}
            }}
        );


        if (!response.ok) {{
            throw new Error(
                "HTTP " + response.status
            );
        }}


        const html =
            await response.text();


        const parser =
            new DOMParser();


        const newDocument =
            parser.parseFromString(
                html,
                "text/html"
            );


        const newHeader =
            newDocument.querySelector(
                ".header"
            );


        const newPlayers =
            newDocument.querySelector(
                ".players"
            );


        const currentHeader =
            document.querySelector(
                ".header"
            );


        const currentPlayers =
            document.querySelector(
                ".players"
            );


        if (
            newHeader &&
            currentHeader
        ) {{

            currentHeader.innerHTML =
                newHeader.innerHTML;

        }}


        if (
            newPlayers &&
            currentPlayers
        ) {{

            currentPlayers.innerHTML =
                newPlayers.innerHTML;

        }}

    }}

    catch (error) {{

        console.log(
            "USER LOG UPDATE ERROR:",
            error
        );

    }}

    finally {{

        updating = false;

    }}

}}


/* =====================================================
   UPDATE EVERY 700ms
   ===================================================== */

setInterval(
    updateUserLog,
    700
);

</script>


</body>

</html>
"""