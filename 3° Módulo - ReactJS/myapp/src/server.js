const express = require("express")
const app = express() 

app.get("/", (req, res) => {
  res.send('servidor rodando')
})

app.listen(3000, (error) => error === false ? console.log('erro no servidor'): console.log('servidor rodando!'))
