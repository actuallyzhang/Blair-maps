import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("contact-form").addEventListener("submit", function (event) {
        event.preventDefault();
        document.getElementById("response-message").style.display = "block";
        setTimeout(() => { //clears stuff out
            document.getElementById("response-message").style.display = "none";
            document.getElementById("contact-form").reset();
        }, 3000);
    });
});