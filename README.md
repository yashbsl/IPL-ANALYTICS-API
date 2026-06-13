# 🏏 IPL Analytics API

A RESTful API built using **Python, Flask, Pandas, and NumPy** that provides analytics and insights from historical Indian Premier League (IPL) match data.

The API allows users to:

* Retrieve all IPL teams
* Compare head-to-head records between any two teams
* Fetch complete match history of any player
* Access IPL data through simple JSON endpoints

---

## 🚀 Live Demo

**Base URL:**
`https://ipl-analytics-api-g7az.onrender.com`

---

## ✨ Features

* 📊 Team information endpoint
* 🤝 Team vs Team head-to-head statistics
* 🏏 Player match history with detailed match information
* ⚡ Fast JSON responses
* 🌐 Deployed on Render
* 🔄 GitHub integrated auto-deployment

---

## 🛠️ Tech Stack

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Programming Language       |
| Flask        | REST API Framework         |
| Pandas       | Data Processing & Analysis |
| NumPy        | Numerical Operations       |
| CSV          | Data Storage               |
| Render       | Cloud Deployment           |
| Git & GitHub | Version Control            |

---

## 📁 Project Structure

```text
IPL-ANALYTICS-API
│
├── app.py
├── ipl.py
├── ipl.csv
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🔗 API Endpoints

### 1. Home Endpoint

**Request**

```http
GET /
```

**Response**

```json
Hello world
```

---

### 2. Get All Teams

**Request**

```http
GET /api/teams
```

**Example**

```http
https://ipl-analytics-api-g7az.onrender.com/api/teams
```

**Response**

```json
{
  "teams": [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bengaluru"
  ]
}
```

---

### 3. Team vs Team Statistics

**Request**

```http
GET /api/teamvteam?team1=<team1>&team2=<team2>
```

**Example**

```http
https://ipl-analytics-api-g7az.onrender.com/api/teamvteam?team1=Mumbai%20Indians&team2=Chennai%20Super%20Kings
```

**Response**

```json
{
  "total_matches": "38",
  "Mumbai Indians": "20",
  "Chennai Super Kings": "18",
  "draw": "0"
}
```

---

### 4. Player Match History

**Request**

```http
GET /api/playermatches?player=<player_name>
```

**Example**

```http
https://ipl-analytics-api-g7az.onrender.com/api/playermatches?player=V%20Kohli
```

**Response**

```json
{
  "player": "V Kohli",
  "matches_played": 252,
  "matches": [
    {
      "match_date": "2024-05-18",
      "season": 2024,
      "team1": "Royal Challengers Bengaluru",
      "team2": "Chennai Super Kings",
      "venue": "M. Chinnaswamy Stadium",
      "city": "Bengaluru",
      "winner": "Royal Challengers Bengaluru",
      "player_of_match": "Faf du Plessis",
      "match_type": "League",
      "result": "runs",
      "result_margin": 27
    }
  ]
}
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/yashbsl/IPL-ANALYTICS-API.git
cd IPL-ANALYTICS-API
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000/
```

---

## 📈 Future Enhancements

* Player career statistics
* Team-wise season performance
* Venue analytics
* Toss impact analysis
* Highest win margins
* Points table generation
* Interactive API documentation using Swagger

---

## 👨‍💻 Author

**Yash Bansal**

* GitHub: https://github.com/yashbsl
* LinkedIn: `https://www.linkedin.com/in/yash-bansal-b33163339/`

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

