const express = require('express');
const { Server } = require('ws');

const app = express();
const server = app.listen(3000, () => console.log('Server started'));
const wss = new Server({ server });

wss.on('connection', ws => {
  ws.on('message', message => {
    const vote = JSON.parse(message);
    // Process vote and update database (mock implementation)
    const updatedVotes = [{ id: 1, option_text: 'Option 1', count: 5 }];
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify({ type: 'UPDATE_VOTE', data: updatedVotes }));
      }
    });
  });
});

app.post('/vote', (req, res) => {
  const { user_id, voting_instance_id, vote_value } = req.body;
  // Save vote to database
  res.status(200).send({ message: 'Vote cast successfully' });
});
