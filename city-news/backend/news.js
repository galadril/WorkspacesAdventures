// news.js

const newsContainer = document.getElementById("news-container");

function renderNews(news) {
    newsContainer.innerHTML = ""; // Clear existing news
    news.forEach((item) => {
        const newsItem = document.createElement("div");
        newsItem.className = "news-item";
        newsItem.textContent = item;
        newsContainer.appendChild(newsItem);
    });
}

// Mock API call
async function fetchNews() {
    try {
        const response = await fetch("/api/news");
        const data = await response.json();
        renderNews(data);
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

// TODO: Add pagination logic here
document.addEventListener("DOMContentLoaded", fetchNews);
