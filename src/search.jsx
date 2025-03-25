import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("room-form").addEventListener("submit", function (event) {
        event.preventDefault(); // prevent form from refreshing the page
        
        let room1 = document.getElementById("room1").value;
        let room2 = document.getElementById("room2").value;
        
        fetch("http://localhost:3000/s_path", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({room1: room1, room2: room2})
        })
        .then(response => response.json())
        .then(data => {
            // update the message on the page
            document.getElementById("response-message").innerText = data.result;
            document.getElementById("response-message").style.display = "block";
        })
    });
});