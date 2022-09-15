"use strict";

function sendMessage(){
  let textBox = document.getElementById("message");
  let message = textBox.value;
  textBox.value = '';
  let data = JSON.stringify({"message" : message});
  ajaxPostRequest ("/addToChat",data,displayChat);
}

function displayChat(response){
  let data = JSON.parse(response);
  let chatHistory = '';
  for (let d of data){
    chatHistory = chatHistory + d['message'] + "<br>";
  }
  let chatDiv = document.getElementById("chat");
  chatDiv['innerHTML'] = chatHistory
  console.log(response);
}