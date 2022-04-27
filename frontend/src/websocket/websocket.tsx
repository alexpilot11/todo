import React, {ChangeEvent, useState} from "react";


export function Websocket(): React.ReactElement {

    const ws: WebSocket = new WebSocket("ws://localhost:8000/ws");

    const [message, setMessage] = useState('');
    const [name, setName] = useState('');


    function onMessage(event: any) {
        setMessage(event.data);
    }

    ws.onmessage = onMessage;

    function sendMessage() {
        console.log(name);
        ws.send(name);
    }

    function handleChange(event: ChangeEvent<HTMLInputElement>) {
        setName(event.target.value);
    }


    return (
        <div>
            <input type="text" id="messageText" placeholder={'Enter your name'} onChange={handleChange} value={name}/>
            <button onClick={sendMessage}>Send</button>
            <div>{message}</div>
        </div>
    )
}