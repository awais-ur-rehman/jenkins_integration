const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 8000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
  console.log("server started");
});

app.post("/submit", (req, res) => {
  const name = req.body.name;
  res.send(`<h1>Hello, ${name}!</h1>`);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
