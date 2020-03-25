from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os
import json
from sqlalchemy import or_
from db import db, app, Journal
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView

ma = Marshmallow(app)


class JournalSchema(ma.ModelSchema):
    class Meta:
        model = Journal


class CustomIDNode(graphene.relay.Node):
    class Meta:
        name = 'IDNode'

    @staticmethod
    def to_global_id(type, id):
        # returns a non-encoded ID
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        model = getattr(graphene.Query, info.field_name).field_type._meta.model
        return model.objects.get(id=global_id)


class JournalObject(SQLAlchemyObjectType):
    class Meta:
        model = Journal
        interfaces = (CustomIDNode, )


class GraphQLquery(graphene.ObjectType):
    all_Journals = SQLAlchemyConnectionField(JournalObject)


graphql_schema = graphene.Schema(query=GraphQLquery)

# Init schema
Journal_schema = JournalSchema()
Journals_schema = JournalSchema(many=True)


@app.route('/journal/<id>', methods=['GET'])
def get_Post(id):
    journal = Journal.query.get(id)
    return Journal_schema.jsonify(journal)


@app.route('/journals', methods=['GET'])
def get_Posts():
    search_term = request.args.get('search')
    if search_term is None:
        search_term = ""
    search = "%{}%".format(search_term)
    journals = Journal.query.filter(or_(Journal.title.like(
        search))).all()

    return Journals_schema.jsonify(journals)


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=graphql_schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()
