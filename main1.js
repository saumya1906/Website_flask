var events=require('events');
var eventEmitter= new events.EventEmitter();
var connectHandler=function connect(){
    console.log('connection successful.');
    eventEmitter.emit('data_received');
}
eventEmitter.on('connection',connectHandler);