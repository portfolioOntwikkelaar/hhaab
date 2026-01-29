const API = "http://127.0.0.1:8000";

async function loadPanel(endpoint, elementId, title) {
  const res = await fetch(API + "/" + endpoint);
  const data = await res.json();

  document.getElementById(elementId).innerHTML = `
    <h2>${title}</h2>

    <div class="glyph">${data.tzolkin.glyph}</div>

    <p class="title">${data.tzolkin.number} ${data.tzolkin.name}</p>
    <p class="desc">${data.tzolkin.meaning}</p>

    <hr/>

    <p class="title">${data.haab.day} ${data.haab.month}</p>
    <p class="desc">${data.haab.meaning}</p>
  `;
}

loadPanel("yesterday", "yesterday", "Gisteren");
loadPanel("today", "today", "Vandaag");
loadPanel("tomorrow", "tomorrow", "Morgen");
