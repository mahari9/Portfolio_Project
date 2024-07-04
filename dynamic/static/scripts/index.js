#!/usr/bin/node
$(document).ready(function () {
const searchIds = {};

const loginBtn = document.querySelector('.login');
const registerBtn = document.querySelector('.register');

loginBtn.addEventListener('click', () => {
  const loginContent = document.querySelector('.dropdown-content');
  loginContent.classList.toggle('show');
});

registerBtn.addEventListener('click', () => {
  const registerContent = document.querySelector('.dropdown-content:nth-child(2)');
  registerContent.classList.toggle('show');
});

const searchInput = document.querySelector('.search input');
const searchBtn = document.querySelector('.search button');

searchBtn.addEventListener('click', () => {
  const searchTerm = searchInput.value;
  // Implement logic to search content based on searchTerm
  alert(`Searching for: ${filter elements}`);
});
