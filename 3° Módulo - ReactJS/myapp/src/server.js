const express = require("express")
const app = express() 
const port = 3000

app.use(express.json())

const meetings = [
  'Aula 01',
  'Aula 02',
  'Aula 03',
]

app.get("/", (req, res) => {
  res.send(meetings)
})

app.get("/:id", (req,res) => {
  const id = req.params.id-1
  const meeting = meetings[id]

  !meeting ? res.send('Aula não encontrada'):res.send(meeting)
})

app.post("/meetings", (req, res) => {
 const meeting = req.body.meeting
 const id = meetings.length

 meetings.push(meeting)
 res.send(`filme ${meeting} com sucesso no id ${id+1}!`)

})

app.listen(port, (err) => !err ? console.log('servidor rodando!'): console.log('erro no servidor'))
