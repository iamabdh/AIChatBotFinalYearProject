package com.example.chatbotandroidapp

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.chatbotandroidapp.Constant.RECEIVE_ID
import com.example.chatbotandroidapp.Constant.SEND_ID
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.message_view.view.*

class RecyclerAdapter(context : Context) : RecyclerView.Adapter<RecyclerAdapter.ViewHolder>() {

    var messagesList = mutableListOf<Message>()

    inner class ViewHolder(itemView : View) : RecyclerView.ViewHolder(itemView){

        init {

        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerAdapter.ViewHolder {
        val v = LayoutInflater.from(parent.context).inflate(R.layout.message_view, parent, false)
        return ViewHolder(v)
    }
    override fun getItemCount(): Int {
        return messagesList.size
    }
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val currentMessage = messagesList[position]

        when(currentMessage.id){
            SEND_ID -> {
                holder.itemView.user_message.apply{
                    text = currentMessage.message
                    visibility = View.VISIBLE
                }
                holder.itemView.bot_message.visibility = View.GONE
            }

            RECEIVE_ID -> {
                holder.itemView.bot_message.apply {
                    text = currentMessage.message
                    visibility = View.VISIBLE
                }
                holder.itemView.user_message.visibility = View.GONE
            }

        }
    }


    fun insertMessage(message: Message) {
        this.messagesList.add(message)
        notifyItemInserted(messagesList.size)
    }


}