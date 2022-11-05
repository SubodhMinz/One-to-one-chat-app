const id = JSON.parse(document.getElementById('id').textContent)
let ws;

if (id){
    ws = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + id + '/'
    )
}else{
    ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/')
}

ws.onopen = ()=>{
    console.log('open...')
}

ws.onmessage = (event)=>{
    console.log('receive...')
    const data = JSON.parse(event.data)
    document.querySelector('#chat-log').value += (data.user + " : " + data.msg + '\n')
}

ws.onerror = (event)=>{
    console.log('error...', event)
}

ws.onclose = (event)=>{
    console.log('close...')
}

document.getElementById('chat-message-submit').onclick =
    function (event){
        const messageInputDom = document.getElementById('chat-message-input')
        const message = messageInputDom.value
        ws.send(JSON.stringify({'msg':message}))
        messageInputDom.value = ''
    }
