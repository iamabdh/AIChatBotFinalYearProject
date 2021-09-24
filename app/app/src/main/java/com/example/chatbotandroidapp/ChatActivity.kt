package com.example.chatbotandroidapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.chatbotandroidapp.Constant.RECEIVE_ID
import com.example.chatbotandroidapp.Constant.SEND_ID
import kotlinx.android.synthetic.main.activity_chat.*


class ChatActivity : AppCompatActivity() {

    var messageList = mutableListOf<Message>()
    private lateinit var adapter: RecyclerAdapter
    private var mSocket : io.socket.client.Socket?= null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_chat)

        SocketHandler.setSocket()
        SocketHandler.establishConnection()
        recyclerView()
        clickEvents()
        mSocket = SocketHandler.getSocket()
        socketResponse()

    }


    private fun clickEvents(){
        send_filed.setOnClickListener {
            sendMessage()
        }
    }

    private fun sendMessage(){
        val message = input_filed.text.toString()

        if (message.isNotEmpty()){
            mSocket?.emit("data", message)
            messageList.add(Message(message, SEND_ID))
            input_filed.setText("")
            adapter.insertMessage(Message(message, SEND_ID))
            rv_messages.scrollToPosition(adapter.itemCount-1)
        }

    }

    private fun recyclerView() {
        adapter = RecyclerAdapter(this)
        rv_messages.adapter = adapter
        rv_messages.layoutManager = LinearLayoutManager(applicationContext)

    }

    private fun socketResponse(){
        mSocket?.on("msgToClient") { res ->
            runOnUiThread {
                botResponse(res[0].toString())
            }
        }
    }

    private fun botResponse(response : String){
        messageList.add(Message(response, RECEIVE_ID))
        adapter.insertMessage(Message(response, RECEIVE_ID))
        rv_messages.scrollToPosition(adapter.itemCount - 1)
    }

}