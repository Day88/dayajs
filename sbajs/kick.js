const thrift = require('thrift-http');
const LineService = require('LineService');

var _client = '';
var gid = '';
var uids = [];
var token = ''; 
var LA = '';

process.argv.forEach(function (val) {
  if(val.includes('gid=')){
	  gid = val.split('gid=').pop();
  }else if(val.includes('uid=')){
	  uids.push(val.split('uid=').pop());
  }else if(val.includes('token=')){
	  token = val.split('token=').pop();
  }else if(val.includes('app=')){
    LA = val.split('app=').pop();
  }
});

function setTHttpClient(options) {
    var connection =
      thrift.createHttpConnection('ga2.line.naver.jp', 443, options);
    connection.on('error', (err) => {
      console.log('err',err);
      return err;
    });
    _client = thrift.createHttpClient(LineService, connection);
  }
  
  
setTHttpClient(options={
    protocol: thrift.TCompactProtocol,
    transport: thrift.TBufferedTransport,
    headers: {'User-Agent':'Line/5.20.2','X-Line-Application':"DESKTOPWIN\t5.20.2\tDESKTOP-1EJCDDQ\t10.0",'X-Line-Access':token},
    path: '/S4',
    https: true
    });
	
for (var i=0; i < uids.length; i++) {
	_client.kickoutFromGroup(0, gid, [uids[i]]);
}