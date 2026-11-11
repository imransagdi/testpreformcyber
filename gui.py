PAGE = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
>

<meta
    name="mobile-web-app-capable"
    content="yes"
>

<meta
    name="apple-mobile-web-app-capable"
    content="yes"
>

<title>CYBER//NET</title>

<style>

/* =====================================================
   RESET
   ===================================================== */

* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html,
body {

    width: 100%;
    height: 100%;

    margin: 0;
    padding: 0;
}

body {

    background: #050605;
    color: #c8c8c8;

    font-family:
        Consolas,
        "Courier New",
        monospace;

    overflow: hidden;

    touch-action: manipulation;
}


/* =====================================================
   TOP BAR
   ===================================================== */

#top {

    height: 44px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 14px;

    background: #090b09;

    border-bottom:
        1px solid #303530;

    flex-shrink: 0;
}

#title {

    color: #8cff8c;

    font-weight: bold;

    letter-spacing: 1px;

    white-space: nowrap;
}

#stats {

    color: #777;

    font-size: 12px;

    white-space: nowrap;

    overflow: hidden;

    text-overflow: ellipsis;

    margin-left: 10px;

    flex: 1;

    text-align: right;
}


/* =====================================================
   USER LOG BUTTON
   ===================================================== */

#user-log-button {

    margin-left: 10px;

    padding: 6px 10px;

    background: #090d09;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    font-size: 10px;

    cursor: pointer;

    min-height: 30px;

    white-space: nowrap;

    flex-shrink: 0;
}

#user-log-button:hover {

    background: #182018;
}


/* =====================================================
   BITCOIN BUTTON
   ===================================================== */

#bitcoin-button {

    margin-left: 10px;

    padding: 6px 10px;

    background: #090d09;

    color: #ffd966;

    border:
        1px solid #7a6a3a;

    font-family: inherit;

    font-size: 10px;

    cursor: pointer;

    min-height: 30px;

    white-space: nowrap;

    flex-shrink: 0;
}

#bitcoin-button:hover {

    background: #201c10;
}


/* =====================================================
   LOGIN
   ===================================================== */

#login {

    position: fixed;

    inset: 0;

    z-index: 100;

    display: flex;

    align-items: center;

    justify-content: center;

    padding: 16px;

    background: #050605;

    overflow-y: auto;
}

#login-box {

    width: min(
        500px,
        100%
    );

    padding: 25px;

    background: #090b09;

    border:
        1px solid #303530;
}

#login-title {

    margin-bottom: 20px;

    color: #8cff8c;

    font-size: 27px;

    font-weight: bold;
}

#name-input,
#room-input,
#language-select {

    width: 100%;

    margin-bottom: 10px;

    padding: 12px;

    background: #050605;

    color: #ddd;

    border:
        1px solid #333;

    outline: none;

    font-family: inherit;

    font-size: 15px;

    border-radius: 0;
}

#account-panel {
    margin: 0 0 14px;
    padding: 13px;
    border: 1px solid #344434;
    background: #070a07;
}

#account-heading {
    margin-bottom: 10px;
    color: #8cff8c;
    font-size: 12px;
    letter-spacing: 2px;
}

#account-username,
#account-password {
    width: 100%;
    margin-bottom: 8px;
    padding: 11px;
    background: #050605;
    color: #ddd;
    border: 1px solid #333;
    outline: none;
    font-family: inherit;
    font-size: 14px;
    border-radius: 0;
}

.account-actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

#account-status {
    margin-top: 9px;
    min-height: 16px;
    color: #9aab9a;
    font-size: 11px;
}

.login-button {

    width: 100%;

    margin-top: 8px;

    padding: 13px;

    background: #0d110d;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    font-size: 14px;

    cursor: pointer;

    min-height: 44px;

    touch-action: manipulation;
}

.login-button:hover {

    background: #182018;
}


/* =====================================================
   LOBBY
   ===================================================== */

#lobby {

    position: fixed;

    inset: 44px 0 0 0;

    z-index: 50;

    display: flex;

    align-items: center;

    justify-content: center;

    padding: 16px;

    background: #050605;

    overflow-y: auto;
}

#lobby-box {

    width: min(
        600px,
        100%
    );

    padding: 24px;

    background: #090b09;

    border:
        1px solid #303530;
}

#lobby-title {

    color: #8cff8c;

    font-size: 24px;

    font-weight: bold;

    margin-bottom: 20px;
}

#room-label {

    color: #777;

    font-size: 12px;
}

#room-code {

    margin: 12px 0;

    color: white;

    font-size: 30px;

    letter-spacing: 6px;

    overflow-wrap: anywhere;
}

#room-help {

    color: #777;

    font-size: 12px;
}

#players {

    margin-top: 20px;

    padding-top: 15px;

    border-top:
        1px solid #292d29;
}

#players-title {

    margin-bottom: 8px;

    color: #777;

    font-size: 12px;
}

.player-entry {

    padding: 8px 0;

    color: #aaa;
}

.player-entry.host {

    color: #8cff8c;
}

#host-play-setting {

    margin-top: 20px;

    padding-top: 15px;

    border-top:
        1px solid #292d29;
}

#host-play-label {

    margin-bottom: 8px;

    color: #777;

    font-size: 12px;
}

#host-play-button {

    width: 100%;

    min-height: 44px;

    padding: 10px;

    background: #101510;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    cursor: pointer;

    touch-action: manipulation;
}

#host-play-button:hover {

    background: #182018;
}

#host-play-button.off {

    background: #120c0c;

    color: #ff9999;

    border-color:
        #704848;
}


/* =====================================================
   GAME TIME
   ===================================================== */

#game-time-setting {

    margin-top: 15px;

    padding-top: 15px;

    border-top:
        1px solid #292d29;
}

#game-time-label {

    margin-bottom: 8px;

    color: #777;

    font-size: 12px;
}

#game-time-select {

    width: 100%;

    min-height: 44px;

    padding: 10px;

    background: #101510;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    font-size: 14px;

    outline: none;
}

#start-game {

    width: 100%;

    margin-top: 25px;

    padding: 14px;

    background: #101510;

    color: #9cff9c;

    border:
        1px solid #789078;

    font-family: inherit;

    cursor: pointer;

    min-height: 48px;

    touch-action: manipulation;
}

#start-game:hover {

    background: #182018;
}

#copy-invite {

    margin-top: 12px;
}


/* =====================================================
   GAME
   ===================================================== */

#game {

    width: 100%;

    height:
        calc(100vh - 44px);

    height:
        calc(100dvh - 44px);

    display: flex;

    flex-direction: column;

    min-height: 0;
}


/* =====================================================
   GAME TIMER
   ===================================================== */

#game-timer {

    color: #9cff9c;

    font-weight: bold;
}


/* =====================================================
   MAP
   ===================================================== */

#map-panel {

    position: relative;

    flex: 1 1 52%;

    min-height: 220px;

    border-bottom:
        1px solid #303530;

    overflow: hidden;
}

.panel-title {

    position: absolute;

    top: 8px;
    left: 10px;

    z-index: 5;

    color: #666;

    font-size: 12px;

    pointer-events: none;
}

#map {

    width: 100%;
    height: 100%;

    display: block;

    touch-action: none;

    user-select: none;

    -webkit-user-select: none;
}


/* =====================================================
   CONNECTION LINES
   ===================================================== */

.connection {

    stroke: #343934;

    stroke-width: 2;

    fill: none;

    pointer-events: none;
}

.connection.player-target {

    stroke: #8cff8c;

    stroke-width: 3;
}


/* =====================================================
   NODES
   ===================================================== */

.player-node {

    cursor: default;

    user-select: none;

    -webkit-user-select: none;
}

.player-node.current {

    cursor: grab;
}

.player-node.current:active {

    cursor: grabbing;
}

.node-circle {

    fill: #080b08;

    stroke: #777;

    stroke-width: 2;
}

.node-circle.mainframe {

    stroke: #ccc;

    stroke-width: 3;
}

.node-circle.player.current {

    stroke: #8cff8c;

    stroke-width: 3;
}

.node-circle.sub-mainframe {

    stroke: #ffcf5a;

    stroke-width: 2;
}

.node-circle.sub-mainframe.breached {

    stroke: #ff5a5a;

    stroke-dasharray: 4 3;
}

.node-text {

    fill: #aaa;

    font-size: 13px;

    text-anchor: middle;

    pointer-events: none;
}

.node-ip {

    fill: #666;

    font-size: 10px;

    text-anchor: middle;

    pointer-events: none;
}


/* =====================================================
   TERMINAL
   ===================================================== */

#terminal-panel {

    height: 48%;

    flex: 1 1 48%;

    min-height: 230px;

    display: flex;

    flex-direction: column;

    background: #030403;

    min-width: 0;

    position: relative;
}

#terminal-title {

    height: 28px;

    flex-shrink: 0;

    padding:
        7px 10px;

    border-bottom:
        1px solid #252925;

    color: #666;

    font-size: 12px;
}

#terminal {

    flex: 1;

    min-height: 0;

    overflow-y: auto;

    padding: 10px;

    white-space: pre-wrap;

    font-size: 13px;

    line-height: 1.45;

    -webkit-overflow-scrolling: touch;
}

.line {

    margin-bottom: 3px;

    overflow-wrap: anywhere;
}

.command {

    color: #ddd;
}

.output {

    color: #aaa;
}

.success {

    color: #9cff9c;
}

.error {

    color: #ff9999;
}

.alert {

    color: white;

    font-weight: bold;
}


/* =====================================================
   TERMINAL INPUT
   ===================================================== */

#input-row {

    min-height: 43px;

    display: flex;

    align-items: center;

    padding: 0 10px;

    border-top:
        1px solid #252925;

    flex-shrink: 0;

    position: relative;
}

#prompt {

    color: #8cff8c;

    white-space: nowrap;

    flex-shrink: 0;
}

#command {

    flex: 1;

    min-width: 0;

    margin-left: 8px;

    background: transparent;

    color: #ddd;

    border: 0;

    outline: 0;

    font-family: inherit;

    font-size: 15px;

    padding: 8px 0;

    border-radius: 0;

    appearance: none;

    position: relative;

    pointer-events: auto;
}


/* =====================================================
   TUTORIAL
   ===================================================== */

#tutorial-button {

    position: absolute;

    top: 7px;
    right: 92px;

    z-index: 10;

    padding: 5px 10px;

    background: #090d09;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    font-size: 11px;

    cursor: pointer;

    min-height: 30px;
}

#tutorial-button:hover {

    background: #182018;
}

#tutorial-overlay {

    position: fixed;

    inset: 0;

    z-index: 300;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 14px;

    background:
        rgba(0, 0, 0, 0.88);

    overflow-y: auto;
}

#tutorial-box {

    width: min(
        700px,
        100%
    );

    max-height: 88vh;

    max-height: 88dvh;

    display: flex;

    flex-direction: column;

    background: #080a08;

    border:
        1px solid #596959;

    min-height: 0;
}

#tutorial-header {

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 14px 16px;

    border-bottom:
        1px solid #303530;

    flex-shrink: 0;
}

#tutorial-title {

    color: #8cff8c;

    font-size: 18px;

    font-weight: bold;
}

#tutorial-close {

    padding: 7px 11px;

    background: transparent;

    color: #aaa;

    border:
        1px solid #555;

    font-family: inherit;

    cursor: pointer;

    min-width: 42px;

    min-height: 36px;
}

#tutorial-content {

    flex: 1;

    overflow-y: auto;

    padding: 25px;

    -webkit-overflow-scrolling: touch;
}

#tutorial-page-title {

    margin-bottom: 20px;

    color: #9cff9c;

    font-size: 20px;
}

#tutorial-text {

    color: #bbb;

    white-space: pre-wrap;

    line-height: 1.65;

    font-size: 14px;
}

#tutorial-footer {

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 10px;

    padding: 12px 16px;

    border-top:
        1px solid #303530;

    flex-shrink: 0;
}

.tutorial-nav {

    min-width: 90px;

    min-height: 42px;

    padding: 10px;

    background: #0d110d;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    cursor: pointer;
}

.tutorial-nav:disabled {

    color: #444;

    border-color: #333;

    cursor: default;
}


/* =====================================================
   ANALYSIS OVERLAY
   ===================================================== */

#analysis-overlay {

    position: fixed;

    inset: 0;

    z-index: 400;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 14px;

    background:
        rgba(0, 0, 0, 0.78);

    overflow-y: auto;

    pointer-events: none;
}

#analysis-box {

    width: min(
        520px,
        100%
    );

    padding: 24px;

    background: #080a08;

    border:
        1px solid #596959;

    pointer-events: none;
}

#analysis-title {

    margin-bottom: 18px;

    color: #9cff9c;

    font-size: 20px;

    font-weight: bold;
}

#analysis-target {

    margin-bottom: 16px;

    color: #aaa;

    font-size: 13px;

    overflow-wrap: anywhere;
}

#analysis-progress {

    width: 100%;

    height: 14px;

    overflow: hidden;

    background: #131713;

    border:
        1px solid #333;
}

#analysis-progress-bar {

    width: 0%;

    height: 100%;

    background: #8cff8c;

    transition: width 0.1s linear;
}

#analysis-countdown {

    margin-top: 12px;

    color: #ddd;

    font-size: 17px;

    text-align: center;
}

#analysis-status {

    margin-top: 14px;

    color: #888;

    font-size: 12px;

    text-align: center;
}


/* =====================================================
   DEFENSE OVERLAY
   ===================================================== */

#defense-overlay {

    position: fixed;

    inset: 0;

    z-index: 410;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 14px;

    background:
        rgba(30, 0, 0, 0.86);

    overflow-y: auto;

    pointer-events: none;
}

#defense-box {

    width: min(
        560px,
        100%
    );

    padding: 24px;

    background: #0b0808;

    border:
        1px solid #a06060;

    pointer-events: none;
}

#defense-overlay * {

    pointer-events: none;
}

#defense-title {

    margin-bottom: 14px;

    color: #ff9999;

    font-size: 25px;

    font-weight: bold;

    letter-spacing: 1px;
}

#defense-message {

    color: #ddd;

    font-size: 14px;

    line-height: 1.6;

    white-space: pre-wrap;
}

#defense-progress {

    margin-top: 18px;

    width: 100%;

    height: 12px;

    overflow: hidden;

    background: #1a1111;

    border:
        1px solid #493333;
}

#defense-progress-bar {

    width: 0%;

    height: 100%;

    background: #ff9999;

    transition: width 0.1s linear;
}

#defense-countdown {

    margin-top: 12px;

    color: #fff;

    font-size: 18px;

    text-align: center;
}

#defense-commands {

    margin-top: 20px;

    padding: 13px;

    background: #100c0c;

    border:
        1px solid #3d2929;

    color: #ffcccc;

    font-size: 14px;

    line-height: 1.7;

    white-space: pre-wrap;
}


/* =====================================================
   BIG IP POPUP
   ===================================================== */

#ip-overlay {

    position: fixed;

    inset: 0;

    z-index: 450;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 20px;

    background:
        rgba(0, 0, 0, 0.92);
}

#ip-box {

    width: min(
        850px,
        96%
    );

    padding: 35px 25px;

    text-align: center;

    background: #080a08;

    border:
        2px solid #596959;

    box-shadow:
        0 0 30px
        rgba(140, 255, 140, 0.08);
}

#ip-player-name {

    margin-bottom: 20px;

    color: #888;

    font-size: 18px;

    font-weight: bold;

    overflow-wrap: anywhere;
}

#ip-value {

    color: #9cff9c;

    font-size: clamp(
        42px,
        10vw,
        96px
    );

    font-weight: bold;

    letter-spacing: 4px;

    line-height: 1.1;

    white-space: nowrap;

    overflow-wrap: anywhere;
}


/* =====================================================
   IP POPUP BUTTONS
   ===================================================== */

#ip-buttons {

    margin-top: 30px;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 10px;

    flex-wrap: wrap;
}

.ip-popup-button {

    min-width: 150px;

    min-height: 50px;

    padding: 12px 20px;

    background: #0d110d;

    color: #9cff9c;

    border:
        1px solid #596959;

    font-family: inherit;

    font-size: 16px;

    cursor: pointer;

    box-sizing: border-box;

    touch-action: manipulation;

    transition:
        background 0.15s,
        border-color 0.15s,
        color 0.15s;
}

.ip-popup-button:hover {

    background: #182018;

    border-color: #789078;

}

.ip-popup-button:active {

    background: #202820;

}

#ip-copy.copied {

    color: #9cff9c;

    border-color: #8cff8c;

    background: #182018;
}


/* =====================================================
   BITCOIN FARM POPUP
   ===================================================== */

#bitcoin-overlay {

    position: fixed;

    inset: 0;

    z-index: 450;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 20px;

    background:
        rgba(0, 0, 0, 0.92);
}

#bitcoin-box {

    width: min(
        420px,
        96%
    );

    padding: 25px;

    text-align: center;

    background: #080a08;

    border:
        2px solid #7a6a3a;

    box-shadow:
        0 0 30px
        rgba(255, 217, 102, 0.08);
}

#bitcoin-title {

    margin-bottom: 20px;

    color: #ffd966;

    font-size: 22px;

    font-weight: bold;

    letter-spacing: 2px;
}

#bitcoin-stats {

    text-align: left;

    border:
        1px solid #303530;

    background: #0c0f0c;

    padding: 14px 16px;

    margin-bottom: 14px;
}

.bitcoin-row {

    display: flex;

    justify-content: space-between;

    padding: 5px 0;

    color: #ccc;

    font-size: 13px;
}

.bitcoin-row span:first-child {

    color: #888;
}

#bitcoin-message {

    min-height: 18px;

    margin-bottom: 12px;

    color: #ff9999;

    font-size: 12px;
}

#bitcoin-buttons {

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 10px;

    flex-wrap: wrap;
}


/* =====================================================
   FINAL LEADERBOARD
   ===================================================== */

#leaderboard-overlay {

    position: fixed;

    inset: 0;

    z-index: 500;

    display: none;

    align-items: center;

    justify-content: center;

    padding: 16px;

    background:
        rgba(0, 0, 0, 0.94);

    overflow-y: auto;
}

#leaderboard-box {

    width: min(
        650px,
        100%
    );

    padding: 25px;

    background: #080a08;

    border:
        2px solid #596959;
}

#leaderboard-title {

    color: #ff9999;

    font-size: 30px;

    font-weight: bold;

    text-align: center;

    letter-spacing: 2px;
}

#leaderboard-subtitle {

    margin-top: 8px;

    margin-bottom: 25px;

    color: #9cff9c;

    text-align: center;

    font-size: 15px;
}

.leaderboard-entry {

    display: grid;

    grid-template-columns:
        50px
        1fr
        110px
        90px;

    gap: 10px;

    align-items: center;

    padding: 12px 8px;

    border-bottom:
        1px solid #292d29;
}

.leaderboard-place {

    color: #9cff9c;

    font-weight: bold;
}

.leaderboard-name {

    color: #ddd;

    overflow-wrap: anywhere;
}

.leaderboard-coins {

    color: #8cff8c;

    text-align: right;
}

.leaderboard-hacks {

    color: #aaa;

    text-align: right;
}


/* =====================================================
   ERROR UI
   ===================================================== */

#error-overlay {

    position: fixed;

    inset: 0;

    z-index: 999998;

    display: none;

    align-items: center;

    justify-content: center;

    background: #000;

    color: #fff;

    font-family:
        Consolas,
        "Courier New",
        monospace;

    font-size: 14px;

    line-height: 1.4;

    text-align: left;

    box-sizing: border-box;

    padding: 20px;
}


#error-text {

    width: auto;

    max-width: 90vw;

    white-space: pre-line;

    color: #fff;

    text-align: left;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (
    max-width: 700px
) {

    #top {

        height: 48px;

        padding:
            0 8px;
    }

    #title {

        font-size: 13px;
    }

    #stats {

        font-size: 8px;

        max-width: 55vw;
    }

    #user-log-button {

        padding:
            5px 7px;

        font-size: 8px;

        margin-left: 5px;

        min-height: 28px;
    }

    #bitcoin-button {

        padding:
            5px 7px;

        font-size: 8px;

        margin-left: 5px;

        min-height: 28px;
    }

    #game {

        height:
            calc(100vh - 48px);

        height:
            calc(100dvh - 48px);
    }

    #map-panel {

        flex:
            1 1 45%;

        min-height: 180px;

        max-height: 50%;
    }

    #terminal-panel {

        flex:
            1 1 55%;

        height: 55%;

        min-height: 240px;
    }

    #terminal {

        font-size: 12px;

        padding: 8px;
    }

    #terminal-title {

        height: 27px;

        padding:
            7px 8px;
    }

    #input-row {

        min-height: 50px;

        padding:
            0 8px;
    }

    #prompt {

        font-size: 12px;
    }

    #command {

        font-size: 16px;

        margin-left: 6px;
    }

    #tutorial-button {

        top: 5px;

        right: 78px;

        padding:
            6px 8px;

        font-size: 9px;
    }

    #login {

        align-items: flex-start;

        padding-top: 35px;
    }

    #login-box {

        padding: 20px;
    }

    #login-title {

        font-size: 24px;
    }

    #lobby {

        align-items: flex-start;

        padding-top: 25px;
    }

    #lobby-box {

        padding: 20px;
    }

    #lobby-title {

        font-size: 21px;
    }

    #room-code {

        font-size: 25px;

        letter-spacing: 4px;
    }

    #tutorial-overlay,
    #analysis-overlay,
    #defense-overlay {

        padding: 8px;
    }

    #tutorial-box {

        max-height: 94vh;

        max-height: 94dvh;
    }

    #tutorial-header {

        padding:
            11px 12px;
    }

    #tutorial-title {

        font-size: 15px;
    }

    #tutorial-content {

        padding: 18px;
    }

    #tutorial-page-title {

        margin-bottom: 14px;

        font-size: 18px;
    }

    #tutorial-text {

        font-size: 13px;

        line-height: 1.55;
    }

    #tutorial-footer {

        padding:
            10px 12px;
    }

    .tutorial-nav {

        min-width: 80px;

        min-height: 44px;
    }

    #analysis-box,
    #defense-box {

        padding: 18px;

        max-height: 92vh;

        max-height: 92dvh;

        overflow-y: auto;
    }

    #analysis-title {

        font-size: 18px;
    }

    #defense-title {

        font-size: 21px;
    }

    #defense-message,
    #defense-commands {

        font-size: 13px;
    }

    #ip-box {

        width: 96%;

        padding:
            28px 15px;
    }

    #ip-player-name {

        font-size: 15px;

        margin-bottom: 18px;
    }

    #ip-value {

        font-size: clamp(
            34px,
            11vw,
            70px
        );

        letter-spacing: 2px;
    }

    #ip-buttons {

        margin-top: 25px;

        flex-direction: column;

        gap: 8px;
    }

    .ip-popup-button {

        width: 100%;

        min-height: 50px;

        margin: 0;
    }

    .leaderboard-entry {

        grid-template-columns:
            35px
            1fr
            80px
            60px;

        font-size: 12px;
    }

    #error-overlay {

        padding: 15px;

        font-size: 11px;

    }

}


/* =====================================================
   VERY SMALL PHONES
   ===================================================== */

@media (
    max-width: 380px
) {

    #stats {

        font-size: 7px;

        max-width: 45vw;
    }

    #user-log-button {

        font-size: 7px;

        padding:
            5px 6px;
    }

    #bitcoin-button {

        font-size: 7px;

        padding:
            5px 6px;
    }

    #map-panel {

        min-height: 160px;
    }

    #terminal-panel {

        min-height: 230px;
    }

    #terminal {

        font-size: 11px;
    }

    #prompt {

        font-size: 10px;
    }

    #command {

        font-size: 16px;
    }

    #login-box,
    #lobby-box {

        padding: 16px;
    }

    #room-code {

        font-size: 21px;

        letter-spacing: 3px;
    }

    #ip-value {

        font-size: 31px;

        letter-spacing: 1px;
    }

}


/* =====================================================
   LANDSCAPE PHONES
   ===================================================== */

@media (
    max-height: 500px
) and (
    max-width: 900px
) {

    #top {

        height: 40px;
    }

    #game {

        height:
            calc(100vh - 40px);

        height:
            calc(100dvh - 40px);
    }

    #map-panel {

        flex:
            1 1 55%;

        min-height: 150px;

        max-height: 60%;
    }

    #terminal-panel {

        flex:
            1 1 45%;

        min-height: 170px;
    }

    #terminal {

        font-size: 11px;
    }

    #input-row {

        min-height: 42px;
    }

}



/* =====================================================
   CRT EFFECT (toggle with the CRT button)
   Pure CSS, no images, no canvas. pointer-events are off,
   so it can never block clicks or taps.
   ===================================================== */

#crt-overlay {

    position: fixed;

    inset: 0;

    /* Above the game, below the crash/error screen (999998)
       so the "restarting..." blackout stays pure black. */
    z-index: 999997;

    pointer-events: none;

    display: none;

    overflow: hidden;
}

body.crt-on #crt-overlay {

    display: block;
}

#crt-overlay div {

    position: absolute;

    inset: 0;
}

/* soft glow on all text while CRT is on (text-shadow is inherited) */
body.crt-on {

    text-shadow:
        0 0 2px rgba(140, 255, 140, 0.35);
}

body.crt-on #title {

    text-shadow:
        0 0 6px rgba(140, 255, 140, 0.55);
}

/* horizontal scanlines */
.crt-scan {

    background:
        repeating-linear-gradient(
            to bottom,
            rgba(0, 0, 0, 0) 0px,
            rgba(0, 0, 0, 0) 2px,
            rgba(0, 0, 0, 0.20) 3px,
            rgba(0, 0, 0, 0) 4px
        );
}

/* faint green phosphor tint */
.crt-tint {

    background: rgba(90, 255, 120, 0.03);
}

/* dark rounded corners, like a curved glass screen */
.crt-vignette {

    background:
        radial-gradient(
            ellipse at center,
            rgba(0, 0, 0, 0) 58%,
            rgba(0, 0, 0, 0.50) 100%
        );

    box-shadow:
        inset 0 0 90px rgba(0, 0, 0, 0.65),
        inset 0 0 5px rgba(140, 255, 140, 0.12);

    border-radius: 14px;
}

/* slow bright band rolling down the screen */
.crt-roll {

    inset: auto 0 auto 0 !important;

    top: -20%;

    height: 18%;

    background:
        linear-gradient(
            to bottom,
            rgba(140, 255, 140, 0),
            rgba(140, 255, 140, 0.05),
            rgba(140, 255, 140, 0)
        );

    animation:
        crtRoll 7s linear infinite;
}

/* very subtle brightness flicker (max 4%) */
.crt-flicker {

    background: #000;

    opacity: 0;

    animation:
        crtFlicker 5s steps(1) infinite;
}

@keyframes crtRoll {

    from { transform: translateY(0); }

    to   { transform: translateY(700%); }
}

@keyframes crtFlicker {

    0%   { opacity: 0; }
    8%   { opacity: 0.03; }
    9%   { opacity: 0; }
    52%  { opacity: 0.02; }
    53%  { opacity: 0; }
    80%  { opacity: 0.04; }
    81%  { opacity: 0; }
}

/* CRT toggle buttons */
#crt-button {

    margin-left: 10px;

    padding: 6px 10px;

    background: #090d09;

    color: #8cff8c;

    border:
        1px solid #3f7a3f;

    font-family: inherit;

    font-size: 10px;

    cursor: pointer;

    min-height: 30px;

    white-space: nowrap;

    flex-shrink: 0;
}

#crt-button:hover {

    background: #142014;
}

#crt-login-button {

    width: 100%;

    margin-top: 10px;

    padding: 10px;

    background: #050605;

    color: #8cff8c;

    border:
        1px solid #3f7a3f;

    font-family: inherit;

    font-size: 12px;

    cursor: pointer;
}

#crt-login-button:hover {

    background: #142014;
}

/* phones: keep it light (no moving layers), smaller button */
@media (
    max-width: 700px
) {

    .crt-roll,
    .crt-flicker {

        display: none;
    }

    #crt-button {

        padding: 5px 7px;

        font-size: 8px;

        margin-left: 5px;

        min-height: 28px;
    }
}

@media (
    max-width: 380px
) {

    #crt-button {

        font-size: 7px;

        padding: 5px 6px;
    }
}

/* respect "reduce motion" system setting */
@media (
    prefers-reduced-motion: reduce
) {

    .crt-roll,
    .crt-flicker {

        display: none;
    }
}


/* =====================================================
   STORE + HARDWARE PANELS
   ===================================================== */
.game-panel-overlay {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 12000;
    align-items: center;
    justify-content: center;
    padding: 14px;
    background: rgba(0, 0, 0, .82);
    backdrop-filter: blur(3px);
}
.game-panel {
    width: min(760px, 100%);
    max-height: min(86vh, 820px);
    overflow: auto;
    border: 1px solid #1d8f4b;
    background: #080d09;
    box-shadow: 0 0 28px rgba(0, 255, 100, .12);
    padding: 18px;
    color: #b8ffc9;
}
.game-panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    border-bottom: 1px solid #1d8f4b;
    padding-bottom: 12px;
    margin-bottom: 14px;
}
.game-panel-title {
    color: #56ff8a;
    font-size: 20px;
    font-weight: bold;
    letter-spacing: 2px;
}
.game-panel-subtitle {
    color: #719b7e;
    font-size: 12px;
    margin-top: 5px;
}
.game-panel-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}
.game-item-card {
    border: 1px solid #244b31;
    background: #0b130d;
    padding: 14px;
    min-width: 0;
}
.game-item-card h3 {
    color: #6aff99;
    margin: 0 0 8px;
    font-size: 15px;
    letter-spacing: 1px;
}
.game-item-card p {
    color: #9ab7a1;
    font-size: 12px;
    line-height: 1.5;
    min-height: 36px;
    margin: 7px 0 12px;
}
.game-item-price {
    color: #e3ff70;
    font-size: 13px;
    margin: 8px 0;
}
.game-item-status {
    color: #8da994;
    font-size: 11px;
    margin: 8px 0;
    overflow-wrap: anywhere;
}
.game-panel-button {
    border: 1px solid #288d4b;
    background: #102718;
    color: #8bffab;
    font-family: inherit;
    font-weight: bold;
    font-size: 12px;
    letter-spacing: 1px;
    padding: 10px 12px;
    cursor: pointer;
    min-height: 38px;
}
.game-panel-button:hover:not(:disabled) {
    background: #174526;
    border-color: #56ff8a;
}
.game-panel-button:disabled {
    opacity: .55;
    cursor: not-allowed;
}
.game-panel-close {
    border-color: #725050;
    background: #201010;
    color: #ffb5b5;
    white-space: nowrap;
}
.game-panel-note {
    color: #739780;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 14px;
}
.hardware-slot {
    text-align: left;
    width: 100%;
    border: 1px solid #275637;
    background: linear-gradient(135deg, #0d1b11, #080d09);
    color: #b8ffc9;
    padding: 14px;
    cursor: pointer;
    font-family: inherit;
}
.hardware-slot.selected {
    border-color: #66ff95;
    box-shadow: inset 0 0 0 1px #1d8f4b, 0 0 12px rgba(0,255,100,.08);
}
.hardware-slot strong {
    display: block;
    color: #67ff98;
    margin-bottom: 8px;
}
.hardware-slot span {
    display: block;
    font-size: 12px;
    color: #92b69c;
    line-height: 1.5;
}

/* PLAYER PROFILE PANEL */
.profile-value {
    color: #e3ff70;
    font-size: 22px;
    font-weight: bold;
    overflow-wrap: anywhere;
}
.profile-hardware-row {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 7px 0;
    border-bottom: 1px solid #1a3322;
    font-size: 12px;
    color: #9ab7a1;
}
.profile-hardware-row:last-child {
    border-bottom: 0;
}
.profile-hardware-row strong {
    color: #6aff99;
    letter-spacing: 1px;
}
#hardware-summary {
    border: 1px dashed #275637;
    padding: 11px;
    color: #d3ffdf;
    font-size: 12px;
    margin-bottom: 12px;
    line-height: 1.6;
}
.hardware-tabs {
    display: flex;
    gap: 8px;
    margin: 0 0 12px;
    border-bottom: 1px solid #244b31;
    padding-bottom: 10px;
}
.hardware-tab-button {
    border: 1px solid #28593a;
    background: #0a160d;
    color: #8eaf99;
    padding: 10px 14px;
    font-family: inherit;
    font-weight: bold;
    font-size: 12px;
    letter-spacing: 1px;
    cursor: pointer;
}
.hardware-tab-button.active {
    color: #7aff9e;
    border-color: #5aff89;
    background: #12331d;
    box-shadow: 0 0 12px rgba(40,255,110,.1);
}
#hardware-message {
    min-height: 22px;
    margin: 8px 0 12px;
    color: #dfff8b;
    font-size: 12px;
    line-height: 1.5;
}
.motherboard-board {
    position: relative;
    border: 2px solid #338354;
    border-radius: 8px;
    padding: 18px;
    margin: 8px 0 14px;
    background:
      radial-gradient(circle at 15% 20%, rgba(60,190,90,.14), transparent 28%),
      linear-gradient(135deg, #0c2a17, #06140b 55%, #0c2414);
    box-shadow: inset 0 0 25px rgba(30,255,100,.08), 0 0 20px rgba(0,0,0,.3);
    overflow: hidden;
}
.motherboard-board:before {
    content: "";
    position: absolute;
    inset: 10px;
    pointer-events: none;
    opacity: .24;
    background-image: linear-gradient(90deg, transparent 49%, #4dbb71 50%, transparent 51%), linear-gradient(0deg, transparent 49%, #4dbb71 50%, transparent 51%);
    background-size: 32px 32px;
}
.motherboard-board > * { position: relative; z-index: 1; }
.motherboard-brand {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    color: #75ff9c;
    border-bottom: 1px solid #36784b;
    padding-bottom: 10px;
    margin-bottom: 16px;
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;
}
.motherboard-layout {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 13px;
    align-items: stretch;
}
.mb-slot-stack { display: grid; gap: 12px; align-content: start; }
.mb-component-slot {
    min-height: 90px;
    border: 1px solid #3b8b55;
    border-radius: 4px;
    background: linear-gradient(135deg, #153d24, #0a1a10);
    color: #baffc9;
    padding: 12px;
    text-align: left;
    width: 100%;
    cursor: context-menu;
    font-family: inherit;
    box-shadow: inset 0 0 0 2px rgba(0,0,0,.24);
}
.mb-component-slot:hover { border-color: #b0ffc3; box-shadow: 0 0 13px rgba(60,255,120,.15); }
.mb-component-slot.occupied { background: linear-gradient(135deg, #1b4d2c, #102318); border-color: #6ad987; }
.mb-component-slot.gpu-slot { min-height: 62px; }
.mb-slot-name { display: block; color: #78ff9e; font-weight: bold; font-size: 12px; letter-spacing: 1px; margin-bottom: 8px; }
.mb-slot-part { display: block; font-size: 13px; color: #e2ffe9; overflow-wrap: anywhere; }
.mb-slot-hint { display: block; margin-top: 7px; color: #88ad93; font-size: 10px; }
.motherboard-badge { color: #e7ff79; font-size: 10px; white-space: nowrap; }
#hardware-inventory-list {
    border: 1px solid #244b31;
    padding: 12px;
    min-height: 55px;
    color: #a7d6b3;
    font-size: 12px;
    line-height: 1.7;
    overflow-wrap: anywhere;
    background: #071009;
}
.hardware-inventory-title { color: #72ff99; font-size: 12px; letter-spacing: 1px; margin: 12px 0 7px; font-weight: bold; }
@media (max-width: 560px) {
    .motherboard-layout { grid-template-columns: 1fr; }
    .motherboard-board { padding: 10px; }
    .mb-component-slot { min-height: 72px; }
    .hardware-tab-button { flex: 1; padding: 9px 5px; }
}
@media (max-width: 560px) {
    .game-panel { padding: 13px; }
    .game-panel-grid { grid-template-columns: 1fr; }
    .game-panel-title { font-size: 17px; }
    .game-item-card p { min-height: 0; }
}

</style>

</head>


<body>

<!-- ===================================================
     CRT OVERLAY
     =================================================== -->

<div id="crt-overlay" aria-hidden="true">
    <div class="crt-tint"></div>
    <div class="crt-scan"></div>
    <div class="crt-roll"></div>
    <div class="crt-flicker"></div>
    <div class="crt-vignette"></div>
</div>



<!-- ===================================================
     TIMER MUSIC (YOUTUBE EMBED)
     ===================================================== -->

<div
    id="youtube-timer-player"
    style="
        position: absolute;
        width: 1px;
        height: 1px;
        opacity: 0;
        pointer-events: none;
        overflow: hidden;
    "
></div>

<script src="https://youtu.be/YeBEctzFvsM?si=bWYcmDq86LdVAlGr"></script>


<!-- ===================================================
     TOP
     =================================================== -->

<header id="top">

    <div id="title">
        CYBER//NET
    </div>

    <div id="stats">

        ROOM:
        <span id="room">
            ------
        </span>

        |

        <span id="player">
            OFFLINE
        </span>

        |

        COINS:
        <span id="coins">
            0
        </span>

        |

        <span id="game-timer">
            TIME: --
        </span>

    </div>

    <button
        id="user-log-button"
        onclick="openUserLog()"
    >
        USER LOG
    </button>

    <button
        id="bitcoin-button"
        onclick="openBitcoinFarm()"
    >
        BITCOIN
    </button>

    <button class="ip-popup-button" onclick="openStorePanel()">STORE</button>
    <button class="ip-popup-button" onclick="openHardwarePanel()">HARDWARE</button>
    <button class="ip-popup-button" onclick="openMotherboardPanel()">MOTHERBOARD</button>
    <button class="ip-popup-button" onclick="openProfilePanel()">PROFILE</button>

    <button
        id="crt-button"
        class="crt-toggle"
        onclick="toggleCrt()"
    >
        CRT: ON
    </button>

</header>


<!-- ===================================================
     LOGIN
     =================================================== -->

<div id="login">

    <div id="login-box">

        <div id="login-title">
            CYBER//NET
        </div>

        <div id="account-panel">
            <div id="account-heading">ACCOUNT ACCESS</div>
            <input id="account-username" placeholder="Username (3–24 characters)" autocomplete="username" maxlength="24">
            <input id="account-password" type="password" placeholder="Password (minimum 8 characters)" autocomplete="current-password">
            <div class="account-actions">
                <button class="login-button" id="account-login-button" onclick="authenticateAccount('login')">LOGIN</button>
                <button class="login-button" id="account-register-button" onclick="authenticateAccount('register')">CREATE ACCOUNT</button>
            </div>
            <div id="account-status">Log in or create an account to continue.</div>
        </div>

        <input
            id="name-input"
            placeholder="Player name (optional; defaults to username)"
            autocomplete="off"
        >

        <input
            id="room-input"
            placeholder="Room code (leave empty to host)"
            autocomplete="off"
            inputmode="numeric"
        >

        <select id="language-select">

            <option value="en">
                English
            </option>

            <option value="ru">
                Русский
            </option>

            <option value="uz">
                O‘zbekcha
            </option>

        </select>

        <button
            id="crt-login-button"
            class="crt-toggle"
            onclick="toggleCrt()"
        >
            CRT: ON
        </button>

        <button
            class="login-button"
            id="enter-button"
            onclick="enterGame()"
        >
            ENTER NETWORK
        </button>

    </div>

</div>


<!-- ===================================================
     LOBBY
     =================================================== -->

<div
    id="lobby"
    style="display:none;"
>

    <div id="lobby-box">

        <div id="lobby-title">
            MULTIPLAYER LOBBY
        </div>

        <div id="room-label">
            ROOM CODE
        </div>

        <div id="room-code">
            ------
        </div>

        <div id="room-help">
            Give this code to your friends.
        </div>

        <button
            id="copy-invite"
            class="login-button"
            onclick="copyInviteLink()"
        >
            COPY INVITE LINK
        </button>

        <div id="players">

            <div id="players-title">
                PLAYERS
            </div>

            <div id="player-list"></div>

        </div>


        <!-- HOST ONLY -->

        <div
            id="host-play-setting"
            style="display:none;"
        >

            <div id="host-play-label">
                HOST WILL PLAY?
            </div>

            <button
                id="host-play-button"
                onclick="toggleHostPlay()"
            >
                YES
            </button>

        </div>


        <!-- GAME TIME -->

        <div
            id="game-time-setting"
            style="display:none;"
        >

            <div id="game-time-label">
                GAME TIME
            </div>

            <select
                id="game-time-select"
                onchange="changeGameTime()"
            >

                <option value="5">
                    5 MINUTES
                </option>

                <option value="10">
                    10 MINUTES
                </option>

                <option value="15" selected>
                    15 MINUTES
                </option>

                <option value="30">
                    30 MINUTES
                </option>

                <option value="60">
                    60 MINUTES
                </option>

            </select>

        </div>


        <button
            id="start-game"
            onclick="startGame()"
            style="display:none;"
        >
            START GAME
        </button>

    </div>

</div>


<!-- ===================================================
     GAME
     =================================================== -->

<div
    id="game"
    style="display:none;"
>

    <section id="map-panel">

        <div class="panel-title">
            NETMAP
        </div>

        <button
            id="tutorial-button"
            onclick="openTutorial()"
        >
            TUTORIAL
        </button>

        <svg
            id="map"
            viewBox="0 0 900 420"
            preserveAspectRatio="xMidYMid meet"
        >
        </svg>

    </section>


    <section id="terminal-panel">

        <div id="terminal-title">
            TERMINAL
        </div>

        <div id="terminal"></div>

        <div id="input-row">

            <span id="prompt">
                guest@cyber:~$
            </span>

            <input
                id="command"
                autocomplete="off"
                autocapitalize="none"
                spellcheck="false"
            >

        </div>

    </section>

</div>


<!-- ===================================================
     TUTORIAL
     =================================================== -->

<div id="tutorial-overlay">

    <div id="tutorial-box">

        <div id="tutorial-header">

            <div id="tutorial-title">
                CYBER//NET TUTORIAL
            </div>

            <button
                id="tutorial-close"
                onclick="closeTutorial()"
            >
                X
            </button>

        </div>

        <div id="tutorial-content">

            <div id="tutorial-page-title"></div>

            <div id="tutorial-text"></div>

        </div>

        <div id="tutorial-footer">

            <button
                id="tutorial-back"
                class="tutorial-nav"
                onclick="tutorialBack()"
            >
                BACK
            </button>

            <div id="tutorial-counter">
                1 / 7
            </div>

            <button
                id="tutorial-next"
                class="tutorial-nav"
                onclick="tutorialNext()"
            >
                NEXT
            </button>

        </div>

    </div>

</div>


<!-- ===================================================
     ANALYSIS OVERLAY
     =================================================== -->

<div id="analysis-overlay">

    <div id="analysis-box">

        <div id="analysis-title">
            ANALYSIS IN PROGRESS
        </div>

        <div id="analysis-target">
            TARGET: UNKNOWN
        </div>

        <div id="analysis-progress">

            <div
                id="analysis-progress-bar"
            ></div>

        </div>

        <div id="analysis-countdown">
            0.0s
        </div>

        <div id="analysis-status">
            Waiting for target response...
        </div>

    </div>

</div>


<!-- ===================================================
     DEFENSE OVERLAY
     =================================================== -->

<div id="defense-overlay">

    <div id="defense-box">

        <div id="defense-title">
            HACKING OCCURRED
        </div>

        <div id="defense-message">
TARGET ANALYSIS DETECTED.

A remote attacker is attempting to analyze your system.

Execute the emergency commands in the correct order before the timer expires.
        </div>

        <div id="defense-progress">

            <div
                id="defense-progress-bar"
            ></div>

        </div>

        <div id="defense-countdown">
            0.0s
        </div>

        <div id="defense-commands">
COMMAND:

2. lock

Enter the commands into your terminal.
        </div>

    </div>

</div>


<!-- ===================================================
     BIG IP POPUP
     =================================================== -->

<div
    id="ip-overlay"
    onclick="closeIPPopup()"
>

    <div
        id="ip-box"
        onclick="event.stopPropagation()"
    >

        <div id="ip-player-name">
            PLAYER
        </div>

        <div id="ip-value">
            0.0.0.0
        </div>

        <div id="ip-buttons">

            <button
                id="ip-copy"
                class="ip-popup-button"
                onclick="copyIP()"
            >
                COPY IP
            </button>

            <button
                id="ip-close"
                class="ip-popup-button"
                onclick="closeIPPopup()"
            >
                CLOSE
            </button>

        </div>

    </div>

</div>


<!-- ===================================================
     FINAL LEADERBOARD
     =================================================== -->

<div
    id="leaderboard-overlay"
>

    <div id="leaderboard-box">

        <div id="leaderboard-title">
            GAME OVER
        </div>

        <div id="leaderboard-subtitle">
            FINAL LEADERBOARD
        </div>

        <div id="leaderboard-list"></div>

    </div>

</div>


<!-- ===================================================
     BITCOIN FARM
     =================================================== -->

<div
    id="bitcoin-overlay"
    onclick="closeBitcoinFarm()"
>

    <div
        id="bitcoin-box"
        onclick="event.stopPropagation()"
    >

        <div id="bitcoin-title">
            BITCOIN FARM
        </div>

        <div id="bitcoin-stats">

            <div class="bitcoin-row">
                <span>GPUs</span>
                <span id="bitcoin-gpus">0</span>
            </div>

            <div class="bitcoin-row">
                <span>INCOME/s</span>
                <span id="bitcoin-income">0</span>
            </div>

            <div class="bitcoin-row">
                <span>ELECTRICITY/s</span>
                <span id="bitcoin-electricity">0</span>
            </div>

            <div class="bitcoin-row">
                <span>NET PROFIT/s</span>
                <span id="bitcoin-profit">0</span>
            </div>

            <div class="bitcoin-row">
                <span>STATUS</span>
                <span id="bitcoin-status">IDLE</span>
            </div>

        </div>

        <div id="bitcoin-message"></div>
        <div style="color:#8ba991;font-size:10px;line-height:1.5;margin:8px 0 12px">
            Bought GPUs enter spare hardware inventory. Open MOTHERBOARD and right-click an empty PCIe slot to install one. Only installed GPUs mine.
        </div>

        <div id="bitcoin-buttons">

            <button
                class="ip-popup-button"
                id="buy-gpu-button"
                onclick="buyGPU()"
            >
                BUY GPU
                (<span id="bitcoin-price">250</span>)
            </button>

            <button
                class="ip-popup-button"
                onclick="closeBitcoinFarm()"
            >
                CLOSE
            </button>

        </div>

    </div>

</div>



<!-- ===================================================
     STORE PANEL
     =================================================== -->
<div id="store-panel" class="game-panel-overlay" onclick="closeGamePanel('store-panel')">
  <section class="game-panel" role="dialog" aria-modal="true" aria-label="CYBER NET Store" onclick="event.stopPropagation()">
    <div class="game-panel-header">
      <div>
        <div class="game-panel-title">CYBER//NET STORE</div>
        <div class="game-panel-subtitle">PERMANENT ITEMS · UPGRADES · BLACK MARKET</div>
      </div>
      <button class="game-panel-button game-panel-close" onclick="closeGamePanel('store-panel')">CLOSE</button>
    </div>
    <div id="store-panel-coins" class="game-panel-subtitle" style="margin-bottom:14px">COINS: --</div>
    <div class="game-panel-grid">
      <article class="game-item-card">
        <h3>DDoS MODULE</h3>
        <div class="game-item-price">2,500 COINS · ONE-TIME PURCHASE</div>
        <p>Temporarily weakens a target's simulated firewall. Ownership never expires.</p>
        <div id="store-ddos-status" class="game-item-status">NOT OWNED</div>
        <button id="store-ddos-button" class="game-panel-button" onclick="buyStoreItem('ddos')">BUY DDoS</button>
      </article>
      <article class="game-item-card">
        <h3>MitM MODULE</h3>
        <div class="game-item-price">2,500 COINS · ONE-TIME PURCHASE</div>
        <p>Uses simulated userdata.dat to intercept half of another player's available coins.</p>
        <div id="store-mitm-status" class="game-item-status">NOT OWNED</div>
        <button id="store-mitm-button" class="game-panel-button" onclick="buyStoreItem('mitm')">BUY MitM</button>
      </article>
      <article class="game-item-card">
        <h3>SPEED UPGRADE</h3>
        <div class="game-item-price">PRICE SHOWN BY GAME</div>
        <p>Improves your analysis speed using the existing upgrade system.</p>
        <button class="game-panel-button" onclick="buyStoreItem('speed')">BUY SPEED</button>
      </article>
      <article class="game-item-card">
        <h3>FIREWALL UPGRADE</h3>
        <div class="game-item-price">PRICE SHOWN BY GAME</div>
        <p>Raises your simulated firewall level.</p>
        <button class="game-panel-button" onclick="buyStoreItem('firewall')">BUY FIREWALL</button>
      </article>
      <article class="game-item-card">
        <h3>EXPLOIT UPGRADE</h3>
        <div class="game-item-price">PRICE SHOWN BY GAME</div>
        <p>Improves your exploit level using the existing upgrade system.</p>
        <button class="game-panel-button" onclick="buyStoreItem('exploit')">BUY EXPLOIT</button>
      </article>
      <article class="game-item-card">
        <h3>BLACK MARKET</h3>
        <div class="game-item-price">EXISTING ITEMS</div>
        <p>Open the original terminal store output for disguise, IP reroll, firewall patch, counter-hack and traceback tools.</p>
        <button class="game-panel-button" onclick="closeGamePanel('store-panel');sendCommand('store')">VIEW IN TERMINAL</button>
      </article>
    </div>
    <div class="game-panel-note">All purchases are validated by the game server. DDoS and MitM ownership is permanent; attack effects and cooldowns are separate.</div>
  </section>
</div>

<!-- ===================================================
     HARDWARE / MOTHERBOARD PANEL
     =================================================== -->
<div id="hardware-panel" class="game-panel-overlay" onclick="closeGamePanel('hardware-panel')">
  <section class="game-panel" role="dialog" aria-modal="true" aria-label="Hardware and motherboard" onclick="event.stopPropagation()">
    <div class="game-panel-header">
      <div>
        <div class="game-panel-title">HARDWARE LAB</div>
        <div class="game-panel-subtitle">BUY COMPONENTS · RIGHT-CLICK A MOTHERBOARD SOCKET TO INSTALL</div>
      </div>
      <button class="game-panel-button game-panel-close" onclick="closeGamePanel('hardware-panel')">CLOSE</button>
    </div>
    <div class="hardware-tabs">
      <button id="hardware-tab-components" class="hardware-tab-button active" onclick="setHardwareTab('components')">COMPONENTS</button>
      <button id="hardware-tab-motherboard" class="hardware-tab-button" onclick="setHardwareTab('motherboard')">MOTHERBOARD</button>
    </div>
    <div id="hardware-summary">CPU Tier 1 | RAM Tier 1 | GPUs 0 | Storage Tier 1</div>
    <div id="hardware-message" aria-live="polite">Buy a component, open MOTHERBOARD, then right-click its matching slot to install.</div>

    <div id="hardware-components-view">
      <div class="game-panel-grid">
        <article class="game-item-card">
          <h3>CPU / PROCESSOR</h3>
          <div class="game-item-price">NEXT COMPONENT: <b id="hardware-cpu-price">250</b> COINS</div>
          <p>Purchase a CPU tier to your spare-parts inventory. Right-click the CPU socket to swap it in.</p>
          <div id="hardware-cpu-detail" class="game-item-status">Installed: Tier 1</div>
          <button class="game-panel-button" onclick="purchaseHardware('cpu')">BUY CPU COMPONENT</button>
        </article>
        <article class="game-item-card">
          <h3>RAM / MEMORY</h3>
          <div class="game-item-price">NEXT COMPONENT: <b id="hardware-ram-price">400</b> COINS</div>
          <p>Purchase a higher-tier memory component. Install it in the RAM socket on the motherboard.</p>
          <div id="hardware-ram-detail" class="game-item-status">Installed: Tier 1</div>
          <button class="game-panel-button" onclick="purchaseHardware('ram')">BUY RAM COMPONENT</button>
        </article>
        <article class="game-item-card">
          <h3>GPU / GRAPHICS</h3>
          <div class="game-item-price">GPU COMPONENT: <b id="hardware-gpu-price">250</b> COINS</div>
          <p>GPUs stay in inventory until installed into a free PCIe slot. Only installed GPUs mine coins.</p>
          <div id="hardware-gpu-detail" class="game-item-status">0 installed · mining accelerator</div>
          <button class="game-panel-button" onclick="buyGPUForHardware()">BUY GPU COMPONENT</button>
        </article>
        <article class="game-item-card">
          <h3>STORAGE / DATA</h3>
          <div class="game-item-price">NEXT COMPONENT: <b id="hardware-storage-price">300</b> COINS</div>
          <p>Purchase a storage component to increase simulated storage capacity when it is installed.</p>
          <div id="hardware-storage-detail" class="game-item-status">Installed: Tier 1</div>
          <button class="game-panel-button" onclick="purchaseHardware('storage')">BUY STORAGE COMPONENT</button>
        </article>
        <article class="game-item-card">
          <h3>MINING STATUS</h3>
          <div id="hardware-mining-detail" class="game-item-status">GPUs: 0 | Income/s: 0 | Electricity/s: 0</div>
          <p>Uninstalled GPUs do not mine. Install GPUs in the motherboard's PCIe slots to activate mining.</p>
          <button class="game-panel-button" onclick="closeGamePanel('hardware-panel');openBitcoinFarm()">OPEN BITCOIN FARM</button>
        </article>
      </div>
    </div>

    <div id="hardware-motherboard-view" style="display:none">
      <div class="motherboard-board">
        <div class="motherboard-brand">
          <span>CYBER//NET MAINBOARD</span>
          <span class="motherboard-badge">REV 1.0 · SIMULATED</span>
        </div>
        <div class="motherboard-layout">
          <div class="mb-slot-stack">
            <button id="mb-slot-cpu" class="mb-component-slot" oncontextmenu="handleBoardRightClick(event, 'cpu')" onclick="handleBoardSlotClick('cpu')" title="Right-click to install or swap CPU">
              <span class="mb-slot-name">CPU SOCKET · AM5</span>
              <span class="mb-slot-part">CPU T1 · INSTALLED</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
            <button id="mb-slot-ram" class="mb-component-slot" oncontextmenu="handleBoardRightClick(event, 'ram')" onclick="handleBoardSlotClick('ram')" title="Right-click to install or swap RAM">
              <span class="mb-slot-name">DIMM · RAM SLOT</span>
              <span class="mb-slot-part">RAM T1 · INSTALLED</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
            <button id="mb-slot-storage" class="mb-component-slot" oncontextmenu="handleBoardRightClick(event, 'storage')" onclick="handleBoardSlotClick('storage')" title="Right-click to install or swap storage">
              <span class="mb-slot-name">M.2 · STORAGE</span>
              <span class="mb-slot-part">STORAGE T1 · INSTALLED</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
          </div>
          <div class="mb-slot-stack">
            <button id="mb-slot-gpu1" class="mb-component-slot gpu-slot" oncontextmenu="handleBoardRightClick(event, 'gpu1')" onclick="handleBoardSlotClick('gpu1')" title="Right-click to install or swap GPU">
              <span class="mb-slot-name">PCIe x16 · GPU 1</span>
              <span class="mb-slot-part">EMPTY PCIe SLOT</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
            <button id="mb-slot-gpu2" class="mb-component-slot gpu-slot" oncontextmenu="handleBoardRightClick(event, 'gpu2')" onclick="handleBoardSlotClick('gpu2')" title="Right-click to install or swap GPU">
              <span class="mb-slot-name">PCIe x16 · GPU 2</span>
              <span class="mb-slot-part">EMPTY PCIe SLOT</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
            <button id="mb-slot-gpu3" class="mb-component-slot gpu-slot" oncontextmenu="handleBoardRightClick(event, 'gpu3')" onclick="handleBoardSlotClick('gpu3')" title="Right-click to install or swap GPU">
              <span class="mb-slot-name">PCIe x1 · GPU 3</span>
              <span class="mb-slot-part">EMPTY PCIe SLOT</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
            <button id="mb-slot-gpu4" class="mb-component-slot gpu-slot" oncontextmenu="handleBoardRightClick(event, 'gpu4')" onclick="handleBoardSlotClick('gpu4')" title="Right-click to install or swap GPU">
              <span class="mb-slot-name">PCIe x1 · GPU 4</span>
              <span class="mb-slot-part">EMPTY PCIe SLOT</span>
              <span class="mb-slot-hint">RIGHT-CLICK TO INSTALL / SWAP</span>
            </button>
          </div>
        </div>
      </div>
      <div class="hardware-inventory-title">SPARE HARDWARE INVENTORY</div>
      <div id="hardware-inventory-list">No spare components yet.</div>
      <div class="game-panel-note">On PC: right-click a socket to install the highest-tier spare component of that type. The current component moves into inventory. On touch screens, tap a socket to install.</div>
    </div>
  </section>
</div>

<!-- ===================================================
     ERROR UI
     =================================================== -->

<div
    id="error-overlay"
>

    <div id="error-text"></div>

</div>


<!-- ===================================================
     PLAYER PROFILE PANEL (READ-ONLY)
     =================================================== -->
<div id="profile-panel" class="game-panel-overlay" onclick="closeProfilePanel()">
  <section class="game-panel" role="dialog" aria-modal="true" aria-label="CYBER NET Player Profile" onclick="event.stopPropagation()">
    <div class="game-panel-header">
      <div>
        <div class="game-panel-title">PLAYER PROFILE</div>
        <div id="profile-status" class="game-panel-subtitle">LOADING...</div>
      </div>
      <button class="game-panel-button game-panel-close" onclick="closeProfilePanel()">CLOSE</button>
    </div>
    <div class="game-panel-grid">
      <article class="game-item-card">
        <h3>USERNAME</h3>
        <div id="profile-username" class="profile-value">--</div>
      </article>
      <article class="game-item-card">
        <h3>REPUTATION (REP)</h3>
        <div id="profile-rep" class="profile-value">--</div>
        <div id="profile-rank" class="game-item-status">--</div>
      </article>
      <article class="game-item-card">
        <h3>COINS</h3>
        <div id="profile-coins" class="profile-value">--</div>
      </article>
      <article class="game-item-card">
        <h3>TOTAL HACKS</h3>
        <div id="profile-hacks" class="profile-value">--</div>
      </article>
      <article class="game-item-card" style="grid-column: 1 / -1">
        <h3>HARDWARE</h3>
        <div class="profile-hardware-row"><strong>CPU</strong><span id="profile-cpu">--</span></div>
        <div class="profile-hardware-row"><strong>RAM</strong><span id="profile-ram">--</span></div>
        <div class="profile-hardware-row"><strong>GPU</strong><span id="profile-gpu">--</span></div>
        <div class="profile-hardware-row"><strong>STORAGE</strong><span id="profile-storage">--</span></div>
      </article>
    </div>
    <div class="game-panel-note">READ-ONLY. REPUTATION AND STATISTICS ARE CALCULATED AND SAVED BY THE SERVER.</div>
  </section>
</div>

<script>

let selectedHardwareSlot = "cpu";

function closeGamePanel(id) {
    const panel = document.getElementById(id);
    if (panel) panel.style.display = "none";
}

/* =====================================================
   PLAYER PROFILE (READ-ONLY)
   ===================================================== */

let profileTimer = null;

function setProfileText(id, text) {
    const element = document.getElementById(id);
    if (element) element.textContent = text;
}

function openProfilePanel() {
    const panel = document.getElementById("profile-panel");
    if (panel) panel.style.display = "flex";
    loadProfile();
    if (profileTimer) clearInterval(profileTimer);
    profileTimer = setInterval(loadProfile, 3000);
}

function closeProfilePanel() {
    if (profileTimer) {
        clearInterval(profileTimer);
        profileTimer = null;
    }
    closeGamePanel("profile-panel");
}

async function loadProfile() {
    const status = document.getElementById("profile-status");

    if (!accountToken) {
        if (status) status.textContent = "LOG IN TO VIEW YOUR PROFILE.";
        return;
    }

    try {
        const query = "?room=" + encodeURIComponent(roomCode || "") +
            "&player=" + encodeURIComponent(playerId || "");
        const response = await fetch("/api/profile" + query, {
            cache: "no-store",
            headers: { "X-Cybernet-Token": accountToken }
        });
        const data = await response.json();

        if (!response.ok || !data.success) {
            if (status) status.textContent = data.error || "UNABLE TO LOAD PROFILE.";
            return;
        }

        renderProfile(data.profile || {});
    } catch (error) {
        console.error(error);
        if (status) status.textContent = "UNABLE TO REACH THE SERVER.";
    }
}

function renderProfile(profile) {
    const hardware = profile.hardware || {};
    const gpus = Number(hardware.gpus || 0);

    setProfileText("profile-username", String(profile.username || "--"));
    setProfileText("profile-rep", Number(profile.reputation || 0).toLocaleString());
    setProfileText("profile-rank", "RANK: " + String(profile.rank || "SCRIPT KIDDIE"));
    setProfileText("profile-coins", Number(profile.coins || 0).toLocaleString());
    setProfileText("profile-hacks", Number(profile.hacks_done || 0).toLocaleString());
    setProfileText("profile-cpu", "TIER " + Number(hardware.cpu_tier || 1));
    setProfileText("profile-ram", "TIER " + Number(hardware.ram_tier || 1));
    setProfileText("profile-gpu", gpus + " INSTALLED");
    setProfileText("profile-storage", "TIER " + Number(hardware.storage_tier || 1));
    setProfileText(
        "profile-status",
        profile.source === "live" ? "LIVE · SYNCED WITH THE SERVER" : "SAVED ACCOUNT DATA"
    );
}

function openStorePanel() {
    refreshGamePanels();
    const panel = document.getElementById("store-panel");
    if (panel) panel.style.display = "flex";
}

function openHardwarePanel() {
    refreshGamePanels();
    const panel = document.getElementById("hardware-panel");
    if (panel) panel.style.display = "flex";
    setHardwareTab("components");
}

function openMotherboardPanel() {
    refreshGamePanels();
    const panel = document.getElementById("hardware-panel");
    if (panel) panel.style.display = "flex";
    setHardwareTab("motherboard");
}

function setHardwareTab(tab) {
    const components = document.getElementById("hardware-components-view");
    const motherboard = document.getElementById("hardware-motherboard-view");
    const componentsButton = document.getElementById("hardware-tab-components");
    const motherboardButton = document.getElementById("hardware-tab-motherboard");
    const showBoard = tab === "motherboard";
    if (components) components.style.display = showBoard ? "none" : "block";
    if (motherboard) motherboard.style.display = showBoard ? "block" : "none";
    if (componentsButton) componentsButton.classList.toggle("active", !showBoard);
    if (motherboardButton) motherboardButton.classList.toggle("active", showBoard);
    renderMotherboard((state && state.player && state.player.hardware) || {});
}

function showHardwareMessage(message, isError = false) {
    const target = document.getElementById("hardware-message");
    if (target) {
        target.textContent = message || "";
        target.style.color = isError ? "#ff9a9a" : "#dfff8b";
    }
}

function updateCoinsInUI(coins) {
    if (state && state.player && Number.isFinite(Number(coins))) state.player.coins = Number(coins);
    const coinsLabel = document.getElementById("coins");
    if (coinsLabel && Number.isFinite(Number(coins))) coinsLabel.textContent = Number(coins).toLocaleString();
}

async function purchaseHardware(part) {
    if (part === "gpu") {
        return buyGPUForHardware();
    }
    if (!roomCode || !playerId) {
        showHardwareMessage("Join a room first.", true);
        return;
    }
    showHardwareMessage("Purchasing " + part.toUpperCase() + " component...");
    try {
        const response = await fetch("/api/hardware/purchase", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({room: roomCode, player: playerId, part})
        });
        const data = await response.json();
        if (!response.ok || !data.success) {
            showHardwareMessage(data.error || "Hardware purchase failed.", true);
        } else {
            updateCoinsInUI(data.coins);
            if (state && state.player && data.hardware) state.player.hardware = data.hardware;
            showHardwareMessage(data.message || "Component added to inventory.");
        }
        refreshGamePanels();
        setTimeout(getState, 100);
    } catch (error) {
        showHardwareMessage("Connection error while buying component.", true);
    }
}

async function buyGPUForHardware() {
    if (!roomCode || !playerId) {
        showHardwareMessage("Join a room first.", true);
        return;
    }
    showHardwareMessage("Buying GPU component...");
    try {
        const response = await fetch("/api/buy-gpu", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({room: roomCode, player: playerId})
        });
        const data = await response.json();
        if (!response.ok || !data.success) {
            showHardwareMessage(data.error || "GPU purchase failed.", true);
        } else {
            updateCoinsInUI(data.coins);
            if (state && state.player && data.hardware) state.player.hardware = data.hardware;
            if (state && state.player && data.bitcoin_farm) state.player.bitcoin_farm = data.bitcoin_farm;
            showHardwareMessage(data.message || "GPU added to spare hardware inventory.");
            if (typeof refreshBitcoinPanel === "function" && data.bitcoin_farm) refreshBitcoinPanel(data.bitcoin_farm);
        }
        refreshGamePanels();
        setTimeout(getState, 100);
    } catch (error) {
        showHardwareMessage("Connection error while buying GPU.", true);
    }
}

async function installHardware(slot) {
    if (!roomCode || !playerId) {
        showHardwareMessage("Join a room first.", true);
        return;
    }
    showHardwareMessage("Installing component in " + slot.toUpperCase() + "...");
    try {
        const response = await fetch("/api/hardware/install", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({room: roomCode, player: playerId, slot})
        });
        const data = await response.json();
        if (!response.ok || !data.success) {
            showHardwareMessage(data.error || "Could not install component.", true);
        } else {
            updateCoinsInUI(data.coins);
            if (state && state.player && data.hardware) state.player.hardware = data.hardware;
            if (state && state.player && data.bitcoin_farm) state.player.bitcoin_farm = data.bitcoin_farm;
            showHardwareMessage(data.message || "Component installed.");
            if (typeof refreshBitcoinPanel === "function" && data.bitcoin_farm) refreshBitcoinPanel(data.bitcoin_farm);
        }
        refreshGamePanels();
        setTimeout(getState, 100);
    } catch (error) {
        showHardwareMessage("Connection error while installing component.", true);
    }
}

function handleBoardRightClick(event, slot) {
    if (event) event.preventDefault();
    installHardware(slot);
    return false;
}

function handleBoardSlotClick(slot) {
    // Right-click is the desktop install gesture. Touchscreens have no right button,
    // so a normal tap installs the component instead.
    if (window.matchMedia && window.matchMedia("(hover: none)").matches) {
        installHardware(slot);
    } else {
        selectedHardwareSlot = slot.startsWith("gpu") ? "gpu" : slot;
        showHardwareMessage("RIGHT-CLICK " + slot.toUpperCase() + " TO INSTALL OR SWAP A SPARE COMPONENT.");
    }
}

function upgradeHardware(part) {
    return purchaseHardware(part);
}

function selectHardwareSlot(part) {
    selectedHardwareSlot = part;
    for (const name of ["cpu", "ram", "gpu", "storage"]) {
        const slot = document.getElementById("hardware-slot-" + name);
        if (slot) slot.classList.toggle("selected", name === part);
    }
    const label = document.getElementById("hardware-selected-slot");
    if (label) label.textContent = "SELECTED: " + part.toUpperCase();
    const action = document.getElementById("hardware-upgrade-button");
    if (action) {
        action.textContent = part === "gpu" ? "BUY GPU COMPONENT" : "BUY " + part.toUpperCase() + " COMPONENT";
        action.disabled = false;
    }
}

function renderMotherboard(hw) {
    const slots = (hw && hw.slots) || {};
    const inventory = (hw && hw.inventory) || [];
    const configs = {
        cpu: {type: "cpu", label: "CPU"},
        ram: {type: "ram", label: "RAM"},
        storage: {type: "storage", label: "STORAGE"},
        gpu1: {type: "gpu", label: "GPU 1"},
        gpu2: {type: "gpu", label: "GPU 2"},
        gpu3: {type: "gpu", label: "GPU 3"},
        gpu4: {type: "gpu", label: "GPU 4"}
    };
    for (const [slotKey, cfg] of Object.entries(configs)) {
        const element = document.getElementById("mb-slot-" + slotKey);
        if (!element) continue;
        const component = slots[slotKey];
        const partLabel = element.querySelector(".mb-slot-part");
        const hint = element.querySelector(".mb-slot-hint");
        element.classList.toggle("occupied", !!component);
        if (partLabel) {
            partLabel.textContent = component
                ? ((component.name || (cfg.label + " T" + (component.tier || 1))) + " · INSTALLED")
                : "EMPTY SLOT · NO COMPONENT";
        }
        if (hint) hint.textContent = component
            ? "RIGHT-CLICK TO REPLACE WITH SPARE"
            : "RIGHT-CLICK TO INSTALL FROM INVENTORY";
    }
    const inventoryBox = document.getElementById("hardware-inventory-list");
    if (inventoryBox) {
        if (!inventory.length) {
            inventoryBox.textContent = "No spare components. Buy CPU, RAM, storage or GPU components in the COMPONENTS tab.";
        } else {
            const counts = {};
            for (const component of inventory) {
                const key = (component.type || "unknown").toUpperCase() + " T" + (component.tier || 1);
                counts[key] = (counts[key] || 0) + 1;
            }
            inventoryBox.textContent = Object.entries(counts)
                .map(([name, count]) => name + " × " + count)
                .join("   |   ");
        }
    }
}

function refreshGamePanels() {
    if (!state || !state.player) return;
    const items = state.player.store_items || {};
    const coins = Number(state.player.coins || 0);
    const coinLabel = document.getElementById("store-panel-coins");
    if (coinLabel) coinLabel.textContent = "AVAILABLE COINS: " + coins.toLocaleString();
    for (const item of ["ddos", "mitm"]) {
        const owned = !!(items[item] && items[item].owned);
        const status = document.getElementById("store-" + item + "-status");
        const button = document.getElementById("store-" + item + "-button");
        if (status) status.textContent = item.toUpperCase() + " — 2,500 coins — " + (owned ? "OWNED PERMANENTLY" : (coins >= 2500 ? "AVAILABLE TO BUY" : "NEED " + (2500 - coins) + " MORE COINS"));
        if (button) {
            button.disabled = owned || coins < 2500;
            button.textContent = owned ? "OWNED PERMANENTLY" : "BUY " + item.toUpperCase() + " · 2,500";
        }
    }
    const hw = state.player.hardware || {};
    const slots = hw.slots || {};
    const inventory = hw.inventory || [];
    const cpu = Number(hw.cpu_level || 1);
    const ram = Number(hw.ram_level || 1);
    const gpus = Number(hw.gpus || 0);
    const storage = Number(hw.storage_level || 1);
    const summary = document.getElementById("hardware-summary");
    if (summary) summary.textContent = "CPU Tier " + cpu + " | RAM Tier " + ram + " (" + (4 * ram) + " GB) | GPUs Installed " + gpus + " | Storage Tier " + storage + " (" + (100 * storage) + " GB) | Spare Parts " + inventory.length;
    const nextTier = (part, currentTier) => {
        let highest = currentTier;
        for (const item of inventory) if (item.type === part) highest = Math.max(highest, Number(item.tier || 1));
        return highest;
    };
    const cpuPrice = 250 * nextTier("cpu", cpu);
    const ramPrice = 400 * nextTier("ram", ram);
    const storagePrice = 300 * nextTier("storage", storage);
    const values = {
        cpu: {detail: "Installed: Tier " + cpu + " · faster simulated analysis", price: cpuPrice},
        ram: {detail: "Installed: Tier " + ram + " · " + (4 * ram) + " GB simulated memory", price: ramPrice},
        gpu: {detail: gpus + " installed · " + inventory.filter(item => item.type === "gpu").length + " spare · mining accelerator", price: Number((state.player.bitcoin_farm || {}).gpu_price || 250)},
        storage: {detail: "Installed: Tier " + storage + " · " + (100 * storage) + " GB simulated storage", price: storagePrice}
    };
    for (const part of ["cpu", "ram", "gpu", "storage"]) {
        const detail = document.getElementById("hardware-" + part + "-detail");
        const price = document.getElementById("hardware-" + part + "-price");
        if (detail) detail.textContent = values[part].detail;
        if (price) price.textContent = values[part].price.toLocaleString();
    }
    const farm = state.player.bitcoin_farm || {};
    const mining = document.getElementById("hardware-mining-detail");
    if (mining) mining.textContent = "Installed GPUs: " + (farm.gpus ?? gpus) + " | Income/s: " + (farm.income_per_second ?? "--") + " | Electricity/s: " + (farm.electricity_per_second ?? "--");
    renderMotherboard(hw);
    selectHardwareSlot(selectedHardwareSlot);
}

/* =====================================================
   GLOBALS
   ===================================================== */

let roomCode = "";
let playerId = "";
let playerName = "";
let accountToken = localStorage.getItem("cybernet_account_token") || "";
let accountUsername = localStorage.getItem("cybernet_account_username") || "";

/* =====================================================
   ACCOUNT TOKEN ON API REQUESTS
   The server uses the login token to confirm which account owns a player.
   ===================================================== */

function expireAccountSession() {
    accountToken = "";
    accountUsername = "";
    localStorage.removeItem("cybernet_account_token");
    localStorage.removeItem("cybernet_account_username");
    const status = document.getElementById("account-status");
    if (status) {
        status.textContent = "SESSION EXPIRED — log in again to load your saved progress.";
    }
}

(function installAccountFetch() {
    const nativeFetch = window.fetch.bind(window);

    window.fetch = function (input, init) {
        let options = init || {};
        const isApiCall = typeof input === "string" && input.startsWith("/api/");

        if (isApiCall && accountToken) {
            const headers = new Headers(options.headers || {});
            if (!headers.has("X-Cybernet-Token")) {
                headers.set("X-Cybernet-Token", accountToken);
            }
            options = Object.assign({}, options, { headers: headers });
        }

        return nativeFetch(input, options).then(function (response) {
            if (
                response.status === 401 &&
                isApiCall &&
                (input.startsWith("/api/create") || input.startsWith("/api/join"))
            ) {
                expireAccountSession();
            }
            return response;
        });
    };
})();

let isHost = false;

let state = null;

let language = "en";

let stateRequestRunning = false;

let tutorialPage = 0;

let seenEvents = new Set();

let draggingPlayer = null;

let dragOffset = {
    x: 0,
    y: 0
};

let analysisTimer = null;

let defenseTimer = null;

let gameTimerInterval = null;

let leaderboardShown = false;

let errorUITimer = null;

let errorUILineTimer = null;


/* =====================================================
   ELEMENTS
   ===================================================== */

const terminal =
    document.getElementById(
        "terminal"
    );

const commandInput =
    document.getElementById(
        "command"
    );

const map =
    document.getElementById(
        "map"
    );


/* =====================================================
   MAP
   ===================================================== */

const MAINFRAME_IP =
    "10.0.0.99";

const MAINFRAME_POSITION = {
    x: 450,
    y: 210
};

const playerPositions = {};

let teamSubPositions = {};


/* =====================================================
   ERROR UI
   ===================================================== */

function showErrorUI() {

    const overlay =
        document.getElementById(
            "error-overlay"
        );

    const text =
        document.getElementById(
            "error-text"
        );

    if (
        !overlay ||
        !text
    ) {

        return;

    }


    const lines = [

        "------------------------",
        "mryovrflw.dll ERR",
        "launching hkload.exe...",
        "launching bootmgr",
        "launching kernel",
        "launching UEFI",
        "launching BIOS",
        "loading...",
        "loading complete!",
        "------------------------"

    ];


    /* Cancel an older error animation */

    if (
        errorUILineTimer
    ) {

        clearTimeout(
            errorUILineTimer
        );

        errorUILineTimer =
            null;

    }


    if (
        errorUITimer
    ) {

        clearTimeout(
            errorUITimer
        );

        errorUITimer =
            null;

    }


    /*
       WHOLE SCREEN BLACK
    */

    overlay.style.display =
        "flex";

    text.textContent =
        "";


    let i = 0;


    function showNextLine() {

        /*
           Add the next line immediately.
        */

        text.textContent +=
            (
                i > 0
                    ? "\n"
                    : ""
            ) +
            lines[i];


        i++;


        /*
           If this was the final line,
           start the EXACT 3 second wait
           immediately.
        */

        if (
            i >=
            lines.length
        ) {

            errorUILineTimer =
                null;


            errorUITimer =
                setTimeout(
                    () => {

                        hideErrorUI();

                    },
                    3000
                );


            return;

        }


        /*
           Random delay between:

           0.10 seconds
           and
           0.25 seconds

           = 100ms - 250ms
        */

        const delay =
            Math.floor(
                Math.random() *
                151
            ) +
            100;


        errorUILineTimer =
            setTimeout(
                showNextLine,
                delay
            );

    }


    /*
       First line appears immediately.
    */

    showNextLine();

}


/*
   Hide the error screen
   and return to the game.
*/

function hideErrorUI() {

    const overlay =
        document.getElementById(
            "error-overlay"
        );

    const text =
        document.getElementById(
            "error-text"
        );


    if (
        errorUILineTimer
    ) {

        clearTimeout(
            errorUILineTimer
        );

        errorUILineTimer =
            null;

    }


    if (
        errorUITimer
    ) {

        clearTimeout(
            errorUITimer
        );

        errorUITimer =
            null;

    }


    if (
        overlay
    ) {

        overlay.style.display =
            "none";

    }


    if (
        text
    ) {

        text.textContent =
            "";

    }

}


/* =====================================================
   ROOM CODE
   ===================================================== */

function getRoomFromURL() {

    const params =
        new URLSearchParams(
            window.location.search
        );

    return (
        params.get("room") || ""
    ).trim();

}


function setRoomInURL(
    room
) {

    const url =
        new URL(
            window.location.href
        );

    url.searchParams.set(
        "room",
        room
    );

    window.history.replaceState(
        {},
        "",
        url
    );

}


/* =====================================================
   DEFAULT PLAYER POSITION
   ===================================================== */

function getDefaultPlayerPosition(
    index,
    total
) {

    const radius =
        150;

    const angle =
        -Math.PI / 2 +
        index *
        Math.PI * 2 /
        Math.max(
            total,
            1
        );

    return {

        x:
            MAINFRAME_POSITION.x +
            Math.cos(angle) *
            radius,

        y:
            MAINFRAME_POSITION.y +
            Math.sin(angle) *
            radius

    };

}


/* =====================================================
   SVG
   ===================================================== */

function createSVG(
    tag,
    attrs
) {

    const element =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            tag
        );

    for (
        const key in attrs
    ) {

        element.setAttribute(
            key,
            attrs[key]
        );

    }

    return element;

}


/* =====================================================
   DRAW LINE
   ===================================================== */

function drawConnection(
    source,
    target,
    extraClass = ""
) {

    if (
        !source ||
        !target
    ) {

        return;

    }

    const line =
        createSVG(
            "line",
            {

                x1:
                    source.x,

                y1:
                    source.y,

                x2:
                    target.x,

                y2:
                    target.y,

                class:
                    "connection " +
                    extraClass

            }
        );

    map.appendChild(
        line
    );

}


/* =====================================================
   GET NODE POSITION
   ===================================================== */

function getNodePosition(
    ip,
    players
) {

    if (
        ip === MAINFRAME_IP
    ) {

        return MAINFRAME_POSITION;

    }

    if (
        teamSubPositions[ip]
    ) {

        return teamSubPositions[ip];

    }

    const player =
        players.find(
            item =>
                item.ip === ip
        );

    if (
        player
    ) {

        return playerPositions[
            player.player_id
        ];

    }

    return null;

}


/* =====================================================
   RENDER MAP
   ===================================================== */

function renderMap(
    data
) {

    if (
        !data ||
        !map
    ) {

        return;

    }

    map.innerHTML =
        "";

    const players =
        data.players || [];

    const connections =
        data.connections || [];

    const currentPlayer =
        data.player || null;


    players.forEach(
        (player, index) => {

            if (
                !playerPositions[
                    player.player_id
                ]
            ) {

                playerPositions[
                    player.player_id
                ] =
                    getDefaultPlayerPosition(
                        index,
                        players.length
                    );

            }

        }
    );


    /* TEAM SUB MAINFRAMES (positions) */

    const subTeams =
        (data.teams || []).filter(
            team => team.sub_ip
        );

    teamSubPositions = {};

    subTeams.forEach(
        (team, index) => {

            const step =
                subTeams.length > 1
                    ? Math.min(0.8, 3.0 / (subTeams.length - 1))
                    : 0;

            const angle =
                -Math.PI / 2 +
                (index - (subTeams.length - 1) / 2) * step;

            teamSubPositions[team.sub_ip] = {
                x: MAINFRAME_POSITION.x + Math.cos(angle) * 95,
                y: MAINFRAME_POSITION.y + Math.sin(angle) * 95
            };

        }
    );


    connections.forEach(
        connection => {

            if (
                !Array.isArray(
                    connection
                )
            ) {

                return;

            }

            if (
                connection.length <
                2
            ) {

                return;

            }

            const source =
                getNodePosition(
                    connection[0],
                    players
                );

            const target =
                getNodePosition(
                    connection[1],
                    players
                );

            if (
                source &&
                target
            ) {

                drawConnection(
                    source,
                    target
                );

            }

        }
    );


    /* PRIVATE PLAYER -> PLAYER LINE */

    if (
        currentPlayer
    ) {

        const targetIP =
            currentPlayer.current_ip;

        if (
            targetIP &&
            targetIP !==
                MAINFRAME_IP &&
            targetIP !==
                currentPlayer.ip
        ) {

            const targetPlayer =
                players.find(
                    player =>
                        player.ip ===
                        targetIP
                );

            if (
                targetPlayer
            ) {

                const source =
                    playerPositions[
                        currentPlayer.player_id
                    ];

                const target =
                    playerPositions[
                        targetPlayer.player_id
                    ];

                if (
                    source &&
                    target
                ) {

                    drawConnection(
                        source,
                        target,
                        "player-target"
                    );

                }

            }

        }

    }


    /* MAINFRAME */

    const mainframeGroup =
        createSVG(
            "g",
            {
                class:
                    "mainframe-node"
            }
        );


    mainframeGroup.appendChild(
        createSVG(
            "circle",
            {

                cx:
                    MAINFRAME_POSITION.x,

                cy:
                    MAINFRAME_POSITION.y,

                r:
                    30,

                class:
                    "node-circle mainframe"

            }
        )
    );


    const mainName =
        createSVG(
            "text",
            {

                x:
                    MAINFRAME_POSITION.x,

                y:
                    MAINFRAME_POSITION.y +
                    47,

                class:
                    "node-text"

            }
        );


    mainName.textContent =
        "MAINFRAME.HOST";


    mainframeGroup.appendChild(
        mainName
    );


    const mainIP =
        createSVG(
            "text",
            {

                x:
                    MAINFRAME_POSITION.x,

                y:
                    MAINFRAME_POSITION.y +
                    61,

                class:
                    "node-ip"

            }
        );


    mainIP.textContent =
        MAINFRAME_IP;


    mainframeGroup.appendChild(
        mainIP
    );


    map.appendChild(
        mainframeGroup
    );


    /* TEAM SUB MAINFRAMES */

    subTeams.forEach(
        team => {

            const position =
                teamSubPositions[team.sub_ip];

            const subGroup =
                createSVG(
                    "g",
                    {
                        class:
                            "sub-mainframe-node"
                    }
                );

            subGroup.appendChild(
                createSVG(
                    "circle",
                    {
                        cx:
                            position.x,
                        cy:
                            position.y,
                        r:
                            16,
                        class:
                            team.breached
                                ? "node-circle sub-mainframe breached"
                                : "node-circle sub-mainframe"
                    }
                )
            );

            const subName =
                createSVG(
                    "text",
                    {
                        x:
                            position.x,
                        y:
                            position.y + 31,
                        class:
                            "node-text"
                    }
                );

            subName.textContent =
                team.sub_name || "SUB.HOST";

            subGroup.appendChild(
                subName
            );

            const subIP =
                createSVG(
                    "text",
                    {
                        x:
                            position.x,
                        y:
                            position.y + 44,
                        class:
                            "node-ip"
                    }
                );

            subIP.textContent =
                team.sub_ip;

            subGroup.appendChild(
                subIP
            );

            map.appendChild(
                subGroup
            );

        }
    );


    /* PLAYER NODES */

    players.forEach(
        player => {

            const position =
                playerPositions[
                    player.player_id
                ];

            if (
                !position
            ) {

                return;

            }


            let circleClass =
                "node-circle player";


            const isCurrentPlayer =
                currentPlayer &&
                player.player_id ===
                currentPlayer.player_id;


            if (
                isCurrentPlayer
            ) {

                circleClass +=
                    " current";

            }


            const group =
                createSVG(
                    "g",
                    {

                        class:
                            isCurrentPlayer
                                ? "player-node current"
                                : "player-node"

                    }
                );


            group.appendChild(
                createSVG(
                    "circle",
                    {

                        cx:
                            position.x,

                        cy:
                            position.y,

                        r:
                            21,

                        class:
                            circleClass

                    }
                )
            );


            const name =
                createSVG(
                    "text",
                    {

                        x:
                            position.x,

                        y:
                            position.y +
                            39,

                        class:
                            "node-text"

                    }
                );


            name.textContent =
                player.name;


            group.appendChild(
                name
            );


            const ip =
                createSVG(
                    "text",
                    {

                        x:
                            position.x,

                        y:
                            position.y +
                            52,

                        class:
                            "node-ip"

                    }
                );


            ip.textContent =
                player.ip;


            group.appendChild(
                ip
            );


            if (
                isCurrentPlayer
            ) {

                group.addEventListener(
                    "pointerdown",
                    event => {

                        startPlayerDrag(
                            event,
                            player
                        );

                    }
                );

            }


            /* Desktop double click */

            let clicks = 0;

            let clickTimer = null;


            group.addEventListener(
                "click",
                () => {

                    clicks++;

                    clearTimeout(
                        clickTimer
                    );

                    clickTimer =
                        setTimeout(
                            () => {

                                clicks = 0;

                            },
                            350
                        );


                    if (
                        clicks === 2
                    ) {

                        showIPPopup(
                            player
                        );

                        clicks = 0;

                    }

                }
            );


            /* Mobile double tap */

            let lastTouchTime = 0;


            group.addEventListener(
                "pointerup",
                event => {

                    if (
                        event.pointerType !==
                        "touch"
                    ) {

                        return;

                    }


                    const now =
                        Date.now();


                    if (
                        now -
                        lastTouchTime <
                        350
                    ) {

                        showIPPopup(
                            player
                        );

                        lastTouchTime =
                            0;

                    }

                    else {

                        lastTouchTime =
                            now;

                    }

                }
            );


            map.appendChild(
                group
            );

        }
    );

}


/* =====================================================
   BIG IP POPUP
   ===================================================== */

function showIPPopup(
    player
) {

    if (
        !player
    ) {

        return;

    }

    document.getElementById(
        "ip-player-name"
    ).textContent =
        player.name ||
        "PLAYER";

    document.getElementById(
        "ip-value"
    ).textContent =
        player.ip ||
        "UNKNOWN";

    const copyButton =
        document.getElementById(
            "ip-copy"
        );

    if (
        copyButton
    ) {

        copyButton.textContent =
            "COPY IP";

        copyButton.classList.remove(
            "copied"
        );

    }

    document.getElementById(
        "ip-overlay"
    ).style.display =
        "flex";

}


function closeIPPopup() {

    document.getElementById(
        "ip-overlay"
    ).style.display =
        "none";

}


/* =====================================================
   COPY IP
   ===================================================== */

async function copyIP() {

    const ip =
        document.getElementById(
            "ip-value"
        ).textContent.trim();


    if (
        !ip ||
        ip === "0.0.0.0" ||
        ip === "UNKNOWN"
    ) {

        return;

    }


    const button =
        document.getElementById(
            "ip-copy"
        );


    try {

        if (
            navigator.clipboard &&
            navigator.clipboard.writeText
        ) {

            await navigator.clipboard.writeText(
                ip
            );

        }

        else {

            throw new Error(
                "Clipboard API unavailable."
            );

        }


        button.textContent =
            "COPIED!";

        button.classList.add(
            "copied"
        );


        setTimeout(
            () => {

                if (
                    button
                ) {

                    button.textContent =
                        "COPY IP";

                    button.classList.remove(
                        "copied"
                    );

                }

            },
            1200
        );

    }

    catch (
        error
    ) {

        try {

            const textArea =
                document.createElement(
                    "textarea"
                );

            textArea.value =
                ip;

            textArea.style.position =
                "fixed";

            textArea.style.left =
                "-9999px";

            textArea.style.top =
                "-9999px";

            document.body.appendChild(
                textArea
            );

            textArea.focus();

            textArea.select();

            document.execCommand(
                "copy"
            );

            textArea.remove();


            button.textContent =
                "COPIED!";

            button.classList.add(
                "copied"
            );


            setTimeout(
                () => {

                    if (
                        button
                    ) {

                        button.textContent =
                            "COPY IP";

                        button.classList.remove(
                            "copied"
                        );

                    }

                },
                1200
            );

        }

        catch (
            fallbackError
        ) {

            console.error(
                fallbackError
            );

            window.prompt(
                "Copy this IP:",
                ip
            );

        }

    }

}


/* =====================================================
   BITCOIN FARM
   ===================================================== */

let bitcoinPanelOpen = false;


function refreshBitcoinPanel(
    farm
) {

    if (
        !farm
    ) {

        return;

    }

    document.getElementById(
        "bitcoin-gpus"
    ).textContent =
        farm.gpus;

    document.getElementById(
        "bitcoin-income"
    ).textContent =
        farm.income_per_second;

    document.getElementById(
        "bitcoin-electricity"
    ).textContent =
        farm.electricity_per_second;

    document.getElementById(
        "bitcoin-profit"
    ).textContent =
        farm.net_profit_per_second;

    document.getElementById(
        "bitcoin-status"
    ).textContent =
        farm.running ?
            "MINING" :
            "IDLE";

    document.getElementById(
        "bitcoin-price"
    ).textContent =
        farm.gpu_price;

}


function openBitcoinFarm() {

    if (
        !roomCode
    ) {

        alert(
            "You are not in a room yet."
        );

        return;

    }

    document.getElementById(
        "bitcoin-message"
    ).textContent =
        "";

    bitcoinPanelOpen =
        true;

    if (
        state &&
        state.player &&
        state.player.bitcoin_farm
    ) {

        refreshBitcoinPanel(
            state.player.bitcoin_farm
        );

    }

    document.getElementById(
        "bitcoin-overlay"
    ).style.display =
        "flex";

}


function closeBitcoinFarm() {

    bitcoinPanelOpen =
        false;

    document.getElementById(
        "bitcoin-overlay"
    ).style.display =
        "none";

}


async function buyGPU() {

    if (
        !roomCode ||
        !playerId
    ) {

        return;

    }

    const messageBox =
        document.getElementById(
            "bitcoin-message"
        );

    messageBox.textContent =
        "";

    try {

        const response =
            await fetch(
                "/api/buy-gpu",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            room:
                                roomCode,

                            player:
                                playerId

                        })

                }
            );

        const data =
            await response.json();

        if (
            !data.success
        ) {

            messageBox.textContent =
                data.error ||
                "Could not buy GPU.";

            if (
                data.bitcoin_farm
            ) {

                refreshBitcoinPanel(
                    data.bitcoin_farm
                );

            }

            return;

        }

        refreshBitcoinPanel(
            data.bitcoin_farm
        );
        if (data.message) {
            messageBox.textContent = data.message;
        }
        if (data.hardware && state && state.player) {
            state.player.hardware = data.hardware;
        }
        if (data.coins !== undefined) {
            updateCoinsInUI(data.coins);
        }
        refreshGamePanels();
        setTimeout(getState, 100);

    }

    catch (
        error
    ) {

        messageBox.textContent =
            "Connection error.";

    }

}


/* =====================================================
   USER LOG
   ===================================================== */

function openUserLog() {

    if (
        !roomCode
    ) {

        alert(
            "You are not in a room yet."
        );

        return;

    }


    const logURL =
        "/loguser?room=" +
        encodeURIComponent(
            roomCode
        );


    window.open(
        logURL,
        "_blank"
    );

}


/* =====================================================
   PLAYER DRAGGING
   ===================================================== */

function getSVGPoint(
    event
) {

    const rect =
        map.getBoundingClientRect();

    return {

        x:
            (
                event.clientX -
                rect.left
            ) *
            900 /
            rect.width,

        y:
            (
                event.clientY -
                rect.top
            ) *
            420 /
            rect.height

    };

}


function startPlayerDrag(
    event,
    player
) {

    if (
        player.player_id !==
        playerId
    ) {

        return;

    }

    event.preventDefault();

    draggingPlayer =
        player;

    const point =
        getSVGPoint(
            event
        );

    const position =
        playerPositions[
            player.player_id
        ];

    dragOffset = {

        x:
            point.x -
            position.x,

        y:
            point.y -
            position.y

    };


    try {

        event.currentTarget.setPointerCapture(
            event.pointerId
        );

    }

    catch (
        error
    ) {

        console.log(
            error
        );

    }

}


function movePlayerDrag(
    event
) {

    if (
        !draggingPlayer
    ) {

        return;

    }

    event.preventDefault();

    const point =
        getSVGPoint(
            event
        );

    let x =
        point.x -
        dragOffset.x;

    let y =
        point.y -
        dragOffset.y;

    x =
        Math.max(
            35,
            Math.min(
                865,
                x
            )
        );

    y =
        Math.max(
            35,
            Math.min(
                385,
                y
            )
        );


    playerPositions[
        draggingPlayer.player_id
    ] = {

        x:
            x,

        y:
            y

    };


    renderMap(
        state
    );

}


function stopPlayerDrag() {

    draggingPlayer =
        null;

}


map.addEventListener(
    "pointermove",
    movePlayerDrag
);

map.addEventListener(
    "pointerup",
    stopPlayerDrag
);

map.addEventListener(
    "pointercancel",
    stopPlayerDrag
);

map.addEventListener(
    "pointerleave",
    stopPlayerDrag
);


/* =====================================================
   ACCOUNT LOGIN / REGISTRATION
   ===================================================== */

async function authenticateAccount(mode) {
    const username = document.getElementById("account-username").value.trim();
    const password = document.getElementById("account-password").value;
    const status = document.getElementById("account-status");
    const buttons = [document.getElementById("account-login-button"), document.getElementById("account-register-button")];

    if (!username || !password) {
        status.textContent = "Enter your username and password.";
        return;
    }

    buttons.forEach(button => button.disabled = true);
    status.textContent = mode === "register" ? "Creating account..." : "Logging in...";

    try {
        const response = await fetch(mode === "register" ? "/api/register" : "/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (!response.ok || !data.success) {
            status.textContent = data.error || "Account request failed.";
            return;
        }

        accountToken = data.token;
        accountUsername = data.username || username;
        localStorage.setItem("cybernet_account_token", accountToken);
        localStorage.setItem("cybernet_account_username", accountUsername);
        document.getElementById("account-password").value = "";
        if (!document.getElementById("name-input").value.trim()) {
            document.getElementById("name-input").value = accountUsername;
        }
        status.textContent = "SIGNED IN AS " + accountUsername + " — you can enter the network.";
    } catch (error) {
        console.error(error);
        status.textContent = "Unable to reach the server.";
    } finally {
        buttons.forEach(button => button.disabled = false);
    }
}

/* =====================================================
   ENTER GAME
   ===================================================== */

async function enterGame() {

    leaderboardShown =
        false;

    hideErrorUI();

    if (!accountToken) {
        alert("Please log in or create an account first.");
        return;
    }

    const name =
        (document.getElementById("name-input").value.trim() || accountUsername);


    const roomInput =
        document.getElementById(
            "room-input"
        ).value.trim();


    language =
        document.getElementById(
            "language-select"
        ).value;


    if (
        !name
    ) {

        alert(
            "Enter your player name."
        );

        return;

    }


    try {

        if (
            roomInput === ""
        ) {

            const response =
                await fetch(
                    "/api/create",
                    {

                        method:
                            "POST",

                        headers: {
                            "Content-Type": "application/json",
                            "X-Cybernet-Token": accountToken
                        },

                        body:
                            JSON.stringify({
                                name:
                                    name
                            })

                    }
                );


            const data =
                await response.json();


            if (
                !data.success
            ) {

                alert(
                    data.error
                );

                return;

            }


            roomCode =
                String(
                    data.room
                );

            playerId =
                data.player;

            playerName =
                name;

            isHost =
                true;

        }

        else {

            const cleanRoom =
                roomInput.replace(
                    /\D/g,
                    ""
                );


            if (
                cleanRoom.length !== 6
            ) {

                alert(
                    "Room code must be 6 digits."
                );

                return;

            }


            const response =
                await fetch(
                    "/api/join",
                    {

                        method:
                            "POST",

                        headers: {
                            "Content-Type": "application/json",
                            "X-Cybernet-Token": accountToken
                        },

                        body:
                            JSON.stringify({

                                room:
                                    cleanRoom,

                                name:
                                    name

                            })

                    }
                );


            const data =
                await response.json();


            if (
                !data.success
            ) {

                alert(
                    data.error
                );

                return;

            }


            roomCode =
                String(
                    data.room
                );

            playerId =
                data.player;

            playerName =
                name;

            isHost =
                false;

        }


        setRoomInURL(
            roomCode
        );


        document.getElementById(
            "login"
        ).style.display =
            "none";


        showLobby();

        await getState();

    }

    catch (
        error
    ) {

        console.error(
            error
        );

        alert(
            "Unable to connect to server."
        );

    }

}


/* =====================================================
   LOBBY
   ===================================================== */

function showLobby() {

    document.getElementById(
        "lobby"
    ).style.display =
        "flex";


    document.getElementById(
        "game"
    ).style.display =
        "none";


    document.getElementById(
        "room-code"
    ).textContent =
        roomCode;

}


function updateLobby() {

    if (
        !state
    ) {

        return;

    }


    const list =
        document.getElementById(
            "player-list"
        );


    list.innerHTML =
        "";


    (
        state.players ||
        []
    ).forEach(
        player => {

            const div =
                document.createElement(
                    "div"
                );


            div.className =
                "player-entry";


            if (
                player.player_id ===
                state.host
            ) {

                div.classList.add(
                    "host"
                );

                div.textContent =
                    player.name +
                    " [HOST]";

            }

            else {

                div.textContent =
                    player.name;

            }


            list.appendChild(
                div
            );

        }
    );


    updateHostPlaySetting();

    updateGameTimeSetting();


    const start =
        document.getElementById(
            "start-game"
        );


    if (
        state.host ===
        playerId &&
        !state.started
    ) {

        start.style.display =
            "block";

    }

    else {

        start.style.display =
            "none";

    }

}


/* =====================================================
   HOST WILL PLAY
   ===================================================== */

function updateHostPlaySetting() {

    const setting =
        document.getElementById(
            "host-play-setting"
        );

    const button =
        document.getElementById(
            "host-play-button"
        );


    if (
        !state ||
        state.host !== playerId ||
        state.started
    ) {

        setting.style.display =
            "none";

        return;

    }


    setting.style.display =
        "block";


    const enabled =
        state.host_will_play !== false;


    button.textContent =
        enabled
            ? "YES"
            : "NO";


    button.classList.toggle(
        "off",
        !enabled
    );

}


async function toggleHostPlay() {

    if (
        !state ||
        state.host !== playerId ||
        state.started
    ) {

        return;

    }


    const current =
        state.host_will_play !== false;


    try {

        const response =
            await fetch(
                "/api/host-play",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            room:
                                roomCode,

                            player:
                                playerId,

                            value:
                                !current

                        })

                }
            );


        const data =
            await response.json();


        if (
            !data.success
        ) {

            alert(
                data.error ||
                "Unable to change host setting."
            );

            return;

        }


        await getState();

    }

    catch (
        error
    ) {

        console.error(
            error
        );

    }

}


/* =====================================================
   GAME TIME SETTING
   ===================================================== */

function updateGameTimeSetting() {

    const setting =
        document.getElementById(
            "game-time-setting"
        );

    const select =
        document.getElementById(
            "game-time-select"
        );

    if (
        !state ||
        state.host !== playerId ||
        state.started
    ) {

        setting.style.display =
            "none";

        return;

    }

    setting.style.display =
        "block";

    select.value =
        String(
            state.game_duration_minutes ||
            15
        );

}


async function changeGameTime() {

    if (
        !state ||
        state.host !== playerId ||
        state.started
    ) {

        return;

    }

    const select =
        document.getElementById(
            "game-time-select"
        );

    const minutes =
        Number(
            select.value
        );

    try {

        const response =
            await fetch(
                "/api/game-time",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            room:
                                roomCode,

                            player:
                                playerId,

                            minutes:
                                minutes

                        })

                }
            );


        const data =
            await response.json();


        if (
            !data.success
        ) {

            alert(
                data.error ||
                "Unable to change game time."
            );

            await getState();

            return;

        }


        await getState();

    }

    catch (
        error
    ) {

        console.error(
            error
        );

    }

}


/* =====================================================
   START
   ===================================================== */

async function startGame() {

    try {

        const response =
            await fetch(
                "/api/start",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            room:
                                roomCode,

                            player:
                                playerId

                        })

                }
            );


        const data =
            await response.json();


        if (
            !data.success
        ) {

            alert(
                data.error
            );

            return;

        }


        await getState();

    }

    catch (
        error
    ) {

        console.error(
            error
        );

    }

}


/* =====================================================
   STATE
   ===================================================== */

async function getState() {

    if (
        !roomCode ||
        !playerId
    ) {

        return;

    }


    if (
        stateRequestRunning
    ) {

        return;

    }


    stateRequestRunning =
        true;


    try {

        const response =
            await fetch(
                "/api/state/" +
                encodeURIComponent(
                    roomCode
                ) +
                "?player=" +
                encodeURIComponent(
                    playerId
                ),
                {
                    cache:
                        "no-store"
                }
            );


        if (
            !response.ok
        ) {

            throw new Error(
                "State request failed."
            );

        }


        const data =
            await response.json();


        if (
            !data.success
        ) {

            throw new Error(
                data.error ||
                "State error."
            );

        }


        state =
            data;

        refreshGamePanels();
        updateStats();

        updateGameTimer();

        checkGameEvents(
            data.events || []
        );

        updateAnalysisState(
            data.analysis || null
        );


        if (
            data.game_over
        ) {

            showLeaderboard(
                data.leaderboard || []
            );

        }


        if (
            data.started
        ) {

            document.getElementById(
                "login"
            ).style.display =
                "none";


            document.getElementById(
                "lobby"
            ).style.display =
                "none";


            document.getElementById(
                "game"
            ).style.display =
                "flex";


            renderMap(
                data
            );


            if (
                !gameTimerInterval
            ) {

                startGameTimerUpdates();

            }

        }

        else {

            hideAnalysis();

            hideDefense();

            showLobby();

            updateLobby();

        }

    }

    catch (
        error
    ) {

        console.error(
            error
        );

    }

    finally {

        stateRequestRunning =
            false;

    }

}


/* =====================================================
   GAME TIMER
   ===================================================== */

let timerMusicStarted = false;

let ytPlayer = null;

let ytPlayerReady = false;


function onYouTubeIframeAPIReady() {

    ytPlayer = new YT.Player(
        "youtube-timer-player",
        {

            videoId:
                "MGk1HMgUe90",

            playerVars: {

                autoplay: 0,

                controls: 0,

                disablekb: 1,

                modestbranding: 1,

                fs: 0

            },

            events: {

                onReady:
                    function () {

                        ytPlayerReady =
                            true;

                    }

            }

        }
    );

}


function playTimerMusic() {

    if (
        !ytPlayerReady ||
        timerMusicStarted
    ) {

        return;

    }

    timerMusicStarted =
        true;

    try {

        ytPlayer.seekTo(
            0,
            true
        );

        ytPlayer.playVideo();

    }

    catch (
        error
    ) {

        // Player wasn't ready yet
        // for some reason — ignore,
        // it will simply not play.

    }

}


function stopTimerMusic() {

    timerMusicStarted =
        false;

    if (
        !ytPlayerReady
    ) {

        return;

    }

    try {

        ytPlayer.pauseVideo();

        ytPlayer.seekTo(
            0,
            true
        );

    }

    catch (
        error
    ) {

        // Nothing to stop — ignore.

    }

}


function updateGameTimer() {

    const timer =
        document.getElementById(
            "game-timer"
        );

    if (
        !timer ||
        !state
    ) {

        return;

    }


    if (
        state.game_over
    ) {

        timer.textContent =
            "TIME: 00:00";

        stopTimerMusic();

        return;

    }


    let seconds =
        Number(
            state.game_time_remaining ||
            0
        );


    seconds =
        Math.max(
            0,
            seconds
        );


    if (
        seconds <= 0
    ) {

        stopTimerMusic();

    }

    else if (
        seconds <= 180
    ) {

        playTimerMusic();

    }

    else {

        // Timer is above 3:00 again
        // (new round) — allow the
        // music to trigger once more
        // the next time it crosses
        // the 3-minute mark.

        timerMusicStarted =
            false;

    }


    const minutes =
        Math.floor(
            seconds /
            60
        );


    const remainingSeconds =
        seconds %
        60;


    timer.textContent =
        "TIME: " +
        String(
            minutes
        ).padStart(
            2,
            "0"
        ) +
        ":" +
        String(
            remainingSeconds
        ).padStart(
            2,
            "0"
        );

}


function startGameTimerUpdates() {

    if (
        gameTimerInterval
    ) {

        clearInterval(
            gameTimerInterval
        );

    }


    gameTimerInterval =
        setInterval(
            () => {

                if (
                    state &&
                    state.started &&
                    !state.game_over
                ) {

                    state.game_time_remaining =
                        Math.max(
                            0,
                            Number(
                                state.game_time_remaining ||
                                0
                            ) - 1
                        );

                }


                updateGameTimer();

            },
            1000
        );

}


/* =====================================================
   COMMAND
   ===================================================== */

async function sendCommand(
    text
) {

    if (
        !text
    ) {

        return;

    }


    /*
       FICTIONAL ERROR UI TEST COMMAND

       This only displays the CYBER//NET
       browser error screen.
    */

    if (
        text.trim().toLowerCase() ===
        "error"
    ) {

        printCommand(
            text
        );

        print(
            "SYSTEM ERROR TRIGGERED.",
            "error"
        );

        showErrorUI();

        return;

    }


    printCommand(
        text
    );


    try {

        const response =
            await fetch(
                "/api/command",
                {

                    method:
                        "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({

                            room:
                                roomCode,

                            player:
                                playerId,

                            command:
                                text

                        })

                }
            );


        const data =
            await response.json();


        const output =
            String(
                data.output ||
                ""
            );


        let type =
            "output";


        const upper =
            output.toUpperCase();


        if (
            upper.includes(
                "ACCESS GRANTED"
            ) ||
            upper.includes(
                "PLAYER BREACHED"
            ) ||
            upper.includes(
                "SYSTEM BREACHED"
            ) ||
            upper.includes(
                "COMPLETE"
            ) ||
            upper.includes(
                "TARGET INTERRUPTED"
            ) ||
            upper.includes(
                "DEFENSE COMMAND ACCEPTED"
            ) ||
            upper.includes(
                "UPGRADE PURCHASED"
            )
        ) {

            type =
                "success";

        }


        if (
            upper.includes(
                "DENIED"
            ) ||
            upper.includes(
                "ERROR"
            ) ||
            upper.includes(
                "REJECTED"
            ) ||
            upper.includes(
                "NOT ENOUGH"
            )
        ) {

            type =
                "error";

        }


        if (
            upper.includes(
                "ALERT"
            )
        ) {

            type =
                "alert";

        }


        if (
            output
        ) {

            print(
                output,
                type
            );

        }


        await getState();

    }

    catch (
        error
    ) {

        console.error(
            error
        );


        print(
            "SERVER CONNECTION ERROR.",
            "error"
        );

    }

}


/* =====================================================
   TERMINAL
   ===================================================== */

function print(
    text,
    type = "output"
) {

    const line =
        document.createElement(
            "div"
        );


    line.className =
        "line " +
        type;


    line.textContent =
        String(
            text ?? ""
        );


    terminal.appendChild(
        line
    );


    terminal.scrollTop =
        terminal.scrollHeight;

}


function printCommand(
    text
) {

    print(
        "> " +
        text,
        "command"
    );

}


commandInput.addEventListener(
    "keydown",
    async event => {

        if (
            event.key !==
            "Enter"
        ) {

            return;

        }


        event.preventDefault();


        const text =
            commandInput.value.trim();


        commandInput.value =
            "";


        if (
            text
        ) {

            await sendCommand(
                text
            );

        }

    }
);


/* =====================================================
   STATS
   ===================================================== */

function updateStats() {

    if (
        !state
    ) {

        return;

    }


    document.getElementById(
        "room"
    ).textContent =
        roomCode;


    if (
        state.player
    ) {

        document.getElementById(
            "player"
        ).textContent =
            state.player.name;


        document.getElementById(
            "coins"
        ).textContent =
            state.player.coins;


        if (
            bitcoinPanelOpen &&
            state.player.bitcoin_farm
        ) {

            refreshBitcoinPanel(
                state.player.bitcoin_farm
            );

        }

    }


    updateGameTimer();

}


/* =====================================================
   ANALYSIS / DEFENSE UI
   ===================================================== */

function hideAnalysis() {

    const overlay =
        document.getElementById(
            "analysis-overlay"
        );


    overlay.style.display =
        "none";


    if (
        analysisTimer
    ) {

        clearInterval(
            analysisTimer
        );

        analysisTimer =
            null;

    }

}


function hideDefense() {

    const overlay =
        document.getElementById(
            "defense-overlay"
        );


    overlay.style.display =
        "none";


    if (
        defenseTimer
    ) {

        clearInterval(
            defenseTimer
        );

        defenseTimer =
            null;

    }

}


/* =====================================================
   FOCUS DEFENSE TERMINAL
   ===================================================== */

function focusDefenseTerminal() {

    const commandInput =
        document.getElementById(
            "command"
        );

    if (
        !commandInput
    ) {

        return;

    }


    commandInput.focus();

}


/* =====================================================
   SHOW ANALYSIS
   ===================================================== */

function showAnalysis(
    analysis
) {

    const overlay =
        document.getElementById(
            "analysis-overlay"
        );

    const target =
        document.getElementById(
            "analysis-target"
        );

    const countdown =
        document.getElementById(
            "analysis-countdown"
        );

    const progressBar =
        document.getElementById(
            "analysis-progress-bar"
        );

    const status =
        document.getElementById(
            "analysis-status"
        );


    overlay.style.display =
        "flex";


    target.textContent =
        "TARGET: " +
        (
            analysis.victim_name ||
            "UNKNOWN"
        ) +
        " [" +
        (
            analysis.victim ||
            "UNKNOWN"
        ) +
        "]";


    const update =
        () => {

            if (
                !state ||
                !state.analysis ||
                state.analysis.role !==
                    "attacker"
            ) {

                hideAnalysis();

                return;

            }


            const remaining =
                Math.max(
                    0,
                    Number(
                        state.analysis.remaining ||
                        0
                    )
                );


            const duration =
                7;


            const percent =
                Math.max(
                    0,
                    Math.min(
                        100,
                        (
                            1 -
                            remaining /
                            duration
                        ) *
                        100
                    )
                );


            progressBar.style.width =
                percent +
                "%";


            countdown.textContent =
                remaining.toFixed(
                    1
                ) +
                "s";


            status.textContent =
                remaining > 0
                    ? "ANALYSIS RUNNING..."
                    : "FINALIZING ANALYSIS...";

        };


    update();


    if (
        analysisTimer
    ) {

        clearInterval(
            analysisTimer
        );

    }


    analysisTimer =
        setInterval(
            update,
            100
        );

}


/* =====================================================
   SHOW DEFENSE
   ===================================================== */

function showDefense(
    analysis
) {

    const overlay =
        document.getElementById(
            "defense-overlay"
        );

    const countdown =
        document.getElementById(
            "defense-countdown"
        );

    const progressBar =
        document.getElementById(
            "defense-progress-bar"
        );


    overlay.style.display =
        "flex";


    focusDefenseTerminal();


    const update =
        () => {

            if (
                !state ||
                !state.analysis ||
                state.analysis.role !==
                    "victim"
            ) {

                hideDefense();

                return;

            }


            const remaining =
                Math.max(
                    0,
                    Number(
                        state.analysis.remaining ||
                        0
                    )
                );


            const progress =
                Number(
                    state.analysis.defense_progress ||
                    0
                );


            const required =
                Array.isArray(
                    state.analysis.required_defense
                )
                    ? state.analysis.required_defense.length
                    : 3;


            const percentage =
                Math.max(
                    0,
                    Math.min(
                        100,
                        progress /
                        Math.max(
                            required,
                            1
                        ) *
                        100
                    )
                );


            progressBar.style.width =
                percentage +
                "%";


            countdown.textContent =
                remaining.toFixed(
                    1
                ) +
                "s";

        };


    update();


    if (
        defenseTimer
    ) {

        clearInterval(
            defenseTimer
        );

    }


    defenseTimer =
        setInterval(
            update,
            100
        );

}


/* =====================================================
   ANALYSIS STATE
   ===================================================== */

function updateAnalysisState(
    analysis
) {

    if (
        !analysis ||
        !analysis.active
    ) {

        hideAnalysis();

        hideDefense();

        return;

    }


    if (
        analysis.role ===
        "attacker"
    ) {

        hideDefense();

        showAnalysis(
            analysis
        );

        return;

    }


    if (
        analysis.role ===
        "victim"
    ) {

        hideAnalysis();

        showDefense(
            analysis
        );

        return;

    }


    hideAnalysis();

    hideDefense();

}


/* =====================================================
   FINAL LEADERBOARD
   ===================================================== */

function showLeaderboard(
    leaderboard
) {

    if (
        leaderboardShown
    ) {

        return;

    }


    leaderboardShown =
        true;


    if (
        gameTimerInterval
    ) {

        clearInterval(
            gameTimerInterval
        );

        gameTimerInterval =
            null;

    }


    const list =
        document.getElementById(
            "leaderboard-list"
        );


    list.innerHTML =
        "";


    if (
        !Array.isArray(
            leaderboard
        ) ||
        leaderboard.length === 0
    ) {

        const empty =
            document.createElement(
                "div"
            );

        empty.className =
            "leaderboard-entry";

        empty.innerHTML =
            "<div></div>" +
            "<div class='leaderboard-name'>" +
            "NO PLAYERS" +
            "</div>";

        list.appendChild(
            empty
        );

    }

    else {

        leaderboard.forEach(
            entry => {

                const row =
                    document.createElement(
                        "div"
                    );

                row.className =
                    "leaderboard-entry";


                const place =
                    document.createElement(
                        "div"
                    );

                place.className =
                    "leaderboard-place";

                place.textContent =
                    "#" +
                    entry.place;


                const name =
                    document.createElement(
                        "div"
                    );

                name.className =
                    "leaderboard-name";

                name.textContent =
                    entry.name;


                const coins =
                    document.createElement(
                        "div"
                    );

                coins.className =
                    "leaderboard-coins";

                coins.textContent =
                    entry.coins +
                    " COINS";


                const hacks =
                    document.createElement(
                        "div"
                    );

                hacks.className =
                    "leaderboard-hacks";

                hacks.textContent =
                    entry.hacks +
                    " HACKS";


                row.appendChild(
                    place
                );

                row.appendChild(
                    name
                );

                row.appendChild(
                    coins
                );

                row.appendChild(
                    hacks
                );


                list.appendChild(
                    row
                );

            }
        );

    }


    document.getElementById(
        "leaderboard-overlay"
    ).style.display =
        "flex";

}


/* =====================================================
   EVENTS
   ===================================================== */

function checkGameEvents(
    events
) {

    if (
        !Array.isArray(
            events
        )
    ) {

        return;

    }


    for (
        const event of events
    ) {

        if (
            !event
        ) {

            continue;

        }


        if (
            event.id &&
            seenEvents.has(
                event.id
            )
        ) {

            continue;

        }


        if (
            event.id
        ) {

            seenEvents.add(
                event.id
            );

        }


        if (
            event.type ===
            "hack_detected"
        ) {

            if (
                event.victim !==
                playerId
            ) {

                continue;

            }


            print(
                "[HACK DETECTED]",
                "error"
            );


            if (
                event.attacker
            ) {

                print(
                    "ATTACKER: " +
                    event.attacker,
                    "error"
                );

            }
print(
    "</coinsoverload " +
    Number(event.remaining || 0) +
    "left/>",
    "error"
);

}

        else if (
            event.type ===
            "alert"
        ) {

            print(
                event.message,
                "alert"
            );

        }


        else if (
            event.type ===
            "analysis_started"
        ) {

            if (
                event.victim !==
                playerId
            ) {

                continue;

            }


            print(
                "HACKING OCCURRED",
                "error"
            );

        }


        else if (
            event.type ===
            "analysis_complete"
        ) {

            if (
                event.attacker !==
                playerId
            ) {

                continue;

            }


            print(
                "ANALYSIS COMPLETE.",
                "success"
            );

            print(
                "TARGET READY.",
                "success"
            );

        }


        else if (
            event.type ===
            "analysis_interrupted"
        ) {

            if (
                event.victim !==
                playerId
            ) {

                continue;

            }


            hideDefense();


            print(
                "ANALYSIS INTERRUPTED.",
                "success"
            );

            print(
                "CONNECTION TERMINATED.",
                "success"
            );

        }


        else if (
            event.type ===
            "analysis_error"
        ) {

            if (
                event.attacker !==
                playerId
            ) {

                continue;

            }


            hideAnalysis();


            print(
                "ERROR: TARGET INTERRUPTED THE ANALYSIS.",
                "error"
            );

            print(
                "HACK FAILED.",
                "error"
            );

        }


        else if (
            event.type ===
            "game_over"
        ) {

            hideAnalysis();

            hideDefense();

            print(
                "GAME OVER",
                "alert"
            );

            print(
                "FINAL LEADERBOARD AVAILABLE.",
                "success"
            );

        }

    }


    if (
        seenEvents.size >
        250
    ) {

        seenEvents =
            new Set(
                Array.from(
                    seenEvents
                ).slice(-100)
            );

    }

}


/* =====================================================
   INVITE
   ===================================================== */

async function copyInviteLink() {

    const link =
        window.location.origin +
        window.location.pathname +
        "?room=" +
        encodeURIComponent(
            roomCode
        );


    try {

        await navigator.clipboard.writeText(
            link
        );

        alert(
            "Invite link copied!"
        );

    }

    catch (
        error
    ) {

        window.prompt(
            "Copy this link:",
            link
        );

    }

}


/* =====================================================
   TUTORIAL
   ===================================================== */

const tutorialPages = [

    {

        title:
            "Getting Started",

        text:
`WELCOME TO CYBER//NET.

This is a fictional multiplayer computer network.

You begin connected to:

MAINFRAME.HOST
10.0.0.99

Use the terminal to explore the network.`

    },

    {

        title:
            "NETMAP",

        text:
`The NETMAP displays the real players in the room.

MAINFRAME.HOST is in the center.

Your player is highlighted.

On desktop or mobile, you can drag your own player node.

Double-click or double-tap another player to display their IP address in a large view.

USER LOG shows the current room's players, coins, and successful hacks.`

    },

    {

        title:
            "Room Code",

        text:
`The host creates a 6-digit room code.

Friends enter that same code to join.

You can also use:

COPY INVITE LINK

to share the room.`

    },

    {

        title:
            "Connect",

        text:
`Connect to a target:

connect <IP>

Example:

connect 10.0.0.160

When you connect to another player, your NETMAP shows your private target line.`

    },

    {

        title:
            "Analyze",

        text:
`Player analysis now takes a few seconds.

Use:

connect <PLAYER IP>
analyze

The target receives:

HACKING OCCURRED

The attacker must wait for the analysis timer to finish.

If the target interrupts the analysis, the attack fails.`

    },

    {

        title:
            "Defend",

        text:
`When another player starts analyzing you, you have a short window to respond.

Enter this command in the terminal:

lock

If the command is completed before the timer expires, the analysis is interrupted.

The attacker receives:

ERROR: TARGET INTERRUPTED THE ANALYSIS.
HACK FAILED.`

    },

    {

        title:
            "Hack",

        text:
`If the analysis finishes successfully:

hack

The target becomes ready to hack.

Firewall levels also matter.

Your exploit level must be at least as high as the target firewall level.

Useful commands:

help
scan
connect <IP>
disconnect
info
ports
probe
analyze
hack
files
read <FILE>
status
players
store
inventory
buy <ITEM>
upgrade coins
upgrade speed
upgrade firewall
upgrade exploit`

    }

];


function openTutorial() {

    tutorialPage =
        0;

    document.getElementById(
        "tutorial-overlay"
    ).style.display =
        "flex";

    renderTutorial();

}


function closeTutorial() {

    document.getElementById(
        "tutorial-overlay"
    ).style.display =
        "none";

    commandInput.focus();

}


function renderTutorial() {

    const page =
        tutorialPages[
            tutorialPage
        ];


    document.getElementById(
        "tutorial-page-title"
    ).textContent =
        page.title;


    document.getElementById(
        "tutorial-text"
    ).textContent =
        page.text;


    document.getElementById(
        "tutorial-counter"
    ).textContent =
        (
            tutorialPage +
            1
        ) +
        " / " +
        tutorialPages.length;


    document.getElementById(
        "tutorial-back"
    ).disabled =
        tutorialPage === 0;


    document.getElementById(
        "tutorial-next"
    ).textContent =
        tutorialPage ===
        tutorialPages.length - 1
            ? "FINISH"
            : "NEXT";

}


function tutorialNext() {

    if (
        tutorialPage >=
        tutorialPages.length - 1
    ) {

        closeTutorial();

        return;

    }


    tutorialPage++;

    renderTutorial();

}


function tutorialBack() {

    if (
        tutorialPage <=
        0
    ) {

        return;

    }


    tutorialPage--;

    renderTutorial();

}


/* =====================================================
   LOAD ROOM CODE FROM URL
   ===================================================== */

const inviteRoom =
    getRoomFromURL();


if (
    /^\d{6}$/.test(
        inviteRoom
    )
) {

    document.getElementById(
        "room-input"
    ).value =
        inviteRoom;

}


/* =====================================================
   POLLING
   ===================================================== */

setInterval(
    getState,
    700
);

/* =====================================================
   INITIAL FOCUS
   ===================================================== */

setTimeout(
    () => {

        document.getElementById(
            "name-input"
        ).focus();

    },
    100
);

</script>


<script>

/* =====================================================
   CRT TOGGLE (separate script block so it always runs)
   ===================================================== */

(function () {

    function applyCrt(on) {

        document.body.classList.toggle("crt-on", on);

        var buttons = document.querySelectorAll(".crt-toggle");

        for (var i = 0; i < buttons.length; i++) {
            buttons[i].textContent = on ? "CRT: ON" : "CRT: OFF";
        }
    }

    var saved = null;

    try {
        saved = localStorage.getItem("cybernet_crt");
    } catch (e) {}

    applyCrt(saved === null ? true : saved === "1");

    window.toggleCrt = function () {

        var now = !document.body.classList.contains("crt-on");

        applyCrt(now);

        try {
            localStorage.setItem("cybernet_crt", now ? "1" : "0");
        } catch (e) {}
    };
 
})();

</script>

</body>

</html>
"""