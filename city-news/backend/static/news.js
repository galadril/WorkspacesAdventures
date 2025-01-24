const newsContainer = document.getElementById("news-container");
const API_HOST = "/api"; // Relative path to API

function renderNews(news) {
    newsContainer.innerHTML = ""; // Clear existing news
    news.forEach((item) => {
        const newsItem = document.createElement("div");
        newsItem.className = "news-item";
        newsItem.textContent = item;
        newsContainer.appendChild(newsItem);
    });
}

async function fetchNews() {
    try {
        const response = await fetch(`${API_HOST}/news`); // Use relative path
        const data = await response.json();
        renderNews(data);
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

document.addEventListener("DOMContentLoaded", fetchNews);
