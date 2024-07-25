// // 5分おきに呼び出される
// function requestGlitch() {
//   const urls = [
//     "https://nosy-occipital-teacher.glitch.me",
//     "https://nosy-occipital-teacher.glitch.me/?client=gas", // 後述
//   ];
//   urls.forEach((url) => {
//     const res = UrlFetchApp.fetch(url, {
//       muteHttpExceptions: true,
//     });
//     console.log(res);
//   });
// }

const Logger = require("nodemon/lib/utils/log")

// // // 設定されているトリガー確認
// // function showTriggers() {
// //   const triggers = ScriptApp.getProjectTriggers()
// //   triggers.forEach(trigger => {
// //     console.log('trigger source id: ' + trigger.getTriggerSourceId())
// //     console.log('handler function: ' + trigger.getHandlerFunction())
// //     console.log('event type: ' + trigger.getEventType())
// //     console.log('----------')
// //   })
// // }

// // // 1回だけ実行
// // // トリガー作成
// // function setTrigger() {
// //   ScriptApp.newTrigger('requestGlitch')
// //   .timeBased()
// //   .everyMinutes(1)








// 5分おきに呼び出される
function requestGlitch() {
    const urls = [
        'https://nosy-occipital-teacher.glitch.me/update',
    ]
    const secretKey = 'your_secret_key_here'

    const timestamp = Math.floor(Date.now() / 1000).toString()
    const token = generateToken(timestamp, secretKey)

    const options = {
        'method': 'post',
        'headers': {
            'Authorization': token,
            'X-Timestamp': timestamp
        }
    }

    try {
        urls.forEach(url => {
            const res = UrlFetchApp.fetch(url, options)
            Logger.log(res.getContentText())
            // console.log(res)          
        })
    } catch (error) {
        Logger.log('Error' + error.toString())
    }
}

function generateToken(timestamp, secretKey) {
    const message = timestamp
    const signature = Utilities.computeHmacSha256Signature(message, secretKey)
    return Utilities.base64Encode(signature)
}

// // 設定されているトリガー確認
// function showTriggers() {
//   const triggers = ScriptApp.getProjectTriggers()
//   triggers.forEach(trigger => {
//     console.log('trigger source id: ' + trigger.getTriggerSourceId())
//     console.log('handler function: ' + trigger.getHandlerFunction())
//     console.log('event type: ' + trigger.getEventType())
//     console.log('----------')
//   })
// }

// // 1回だけ実行
// // トリガー作成
// function setTrigger() {
//   ScriptApp.newTrigger('requestGlitch')
//   .timeBased()
//   .everyMinutes(1)