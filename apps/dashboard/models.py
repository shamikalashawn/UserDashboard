#dashboard
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..LogReg.models import userDB

# Create your models here.
class messageManager(models.Manager):
    def message_check(self, data, owner_id, author):
        errors = []
        if len(data['message']) < 1:
            errors.append('message', 'Message must be entered.')

        if errors:
            return [False, errors]
        else:
            #author will be in session and can be passed in from views
            #owner_id will be passed into the url
            owner = userDB.objects.get(id=owner_id)
            newMessage = Message.objects.create(message=data['message'], author=author, owner=owner)
            return [True]

class commentManager(models.Manager):
    def comment_check(self, data, owner_id, author, message_id):
        errors = []
        if len(data['comment']) < 1:
            errors.append('comment', 'Comment must be entered.')

        if errors:
            return [False, errors]
        else:
            #author will be in session and can be passed in
            #owner_id and message_id will be passed into the url
            owner = userDB.objects.get(id=owner_id)
            message = Message.objects.get(id=message_id)
            newComment = Comment.objects.create(comment=data['comment'], author=author, owner=owner, message=message)
            return [True]

class Message(models.Model):
    message = models.TextField()
    author = models.ForeignKey(userDB, related_name='message_author')
    owner = models.ForeignKey(userDB, related_name='message_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = messageManager()

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name='comment_message')
    author = models.ForeignKey(userDB, related_name='comment_author')
    owner = models.ForeignKey(userDB, related_name='comment_owner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = commentManager()
