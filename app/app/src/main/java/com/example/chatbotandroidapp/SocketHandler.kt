package com.example.chatbotandroidapp

import io.socket.client.IO
import io.socket.client.Socket
import java.net.URISyntaxException

object SocketHandler {

    lateinit var mSocket : Socket

    fun setSocket(){
        try {
            mSocket = IO.socket("https://project-gpjma.run-us-west2.goorm.io")
        } catch (e:Exception){

        }
    }
    fun getSocket () : Socket {
        return mSocket
    }
    fun establishConnection() {
        mSocket.connect()
    }
    fun closeConnection() {
        mSocket.disconnect()
    }
}