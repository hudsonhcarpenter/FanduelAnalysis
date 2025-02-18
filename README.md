
<h1>FanDuel Sports Podcast Analysis</h1>

<h2>Description</h2>
This project involves automated web scraping to collect podcast transcripts from Podscribe.ai using the Selenium web automation framework. The script extracts episode links, navigates through paginated content, and retrieves only the sponsored Fanduel segments of the transcripts. I'm currently implementing the ChatGPT API to analyze the outcomes of the podcaster's sports betting picks in these sponsored segments to determine if his paid promotion of sports gambling in this way is harmful.
<br />
<h2>Key Features and Workflow</h2>

<div class="section">
        <h2>✅ Episode Link Extraction</h2>
        <p>The script launches a Chrome WebDriver and navigates to the podcast's episode list page.</p>
        <p>It identifies and collects episode URLs by searching for anchor (<code>&lt;a&gt;</code>) elements containing “episode” in their links.</p>
        <p>If multiple pages exist, it navigates through them using the "Next Page" button until all links are gathered.</p>
    </div>
    <div class="section">
        <h2>✅ Transcript Scraping</h2>
        <p>For each extracted episode link, a new Chrome WebDriver session opens the episode page.</p>
        <p>The script waits for the "Published" date to become visible and extracts it.</p>
        <p>It then searches for transcript sections that contain the keyword <strong>"FanDuel"</strong> and stores them.</p>
    </div>
    <div class="section">
        <h2>✅ Data Storage</h2>
        <p>The extracted transcripts and their respective publication dates are saved in a CSV file (<code>transcripts2.csv</code>) for further analysis.</p>
    </div>
