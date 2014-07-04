# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Match', fields ['group_name']
        db.create_index(u'goalserve_match', ['group_name'])

        # Adding index on 'Match', fields ['week_number']
        db.create_index(u'goalserve_match', ['week_number'])

        # Adding index on 'Match', fields ['g_static_id']
        db.create_index(u'goalserve_match', ['g_static_id'])

        # Adding index on 'Match', fields ['g_id']
        db.create_index(u'goalserve_match', ['g_id'])

        # Adding index on 'F1Results', fields ['g_static_id']
        db.create_index(u'goalserve_f1results', ['g_static_id'])

        # Adding index on 'F1Results', fields ['g_id']
        db.create_index(u'goalserve_f1results', ['g_id'])

        # Adding index on 'F1Commentary', fields ['g_static_id']
        db.create_index(u'goalserve_f1commentary', ['g_static_id'])

        # Adding index on 'F1Commentary', fields ['g_id']
        db.create_index(u'goalserve_f1commentary', ['g_id'])

        # Adding index on 'Stadium', fields ['g_static_id']
        db.create_index(u'goalserve_stadium', ['g_static_id'])

        # Adding index on 'Stadium', fields ['g_id']
        db.create_index(u'goalserve_stadium', ['g_id'])

        # Adding index on 'Stadium', fields ['name']
        db.create_index(u'goalserve_stadium', ['name'])

        # Adding index on 'MatchCommentary', fields ['g_static_id']
        db.create_index(u'goalserve_matchcommentary', ['g_static_id'])

        # Adding index on 'MatchCommentary', fields ['g_id']
        db.create_index(u'goalserve_matchcommentary', ['g_id'])

        # Adding index on 'MatchStandings', fields ['group']
        db.create_index(u'goalserve_matchstandings', ['group'])

        # Adding index on 'MatchStandings', fields ['g_static_id']
        db.create_index(u'goalserve_matchstandings', ['g_static_id'])

        # Adding index on 'MatchStandings', fields ['g_id']
        db.create_index(u'goalserve_matchstandings', ['g_id'])

        # Adding index on 'MatchStandings', fields ['round']
        db.create_index(u'goalserve_matchstandings', ['round'])

        # Adding index on 'MatchEvent', fields ['g_id']
        db.create_index(u'goalserve_matchevent', ['g_id'])

        # Adding index on 'MatchEvent', fields ['g_static_id']
        db.create_index(u'goalserve_matchevent', ['g_static_id'])

        # Adding index on 'MatchEvent', fields ['event_type']
        db.create_index(u'goalserve_matchevent', ['event_type'])

        # Adding index on 'Driver', fields ['g_static_id']
        db.create_index(u'goalserve_driver', ['g_static_id'])

        # Adding index on 'Driver', fields ['g_id']
        db.create_index(u'goalserve_driver', ['g_id'])

        # Adding index on 'Category', fields ['display_name']
        db.create_index(u'goalserve_category', ['display_name'])

        # Adding index on 'Category', fields ['g_static_id']
        db.create_index(u'goalserve_category', ['g_static_id'])

        # Adding index on 'Category', fields ['g_id']
        db.create_index(u'goalserve_category', ['g_id'])

        # Adding index on 'Category', fields ['name']
        db.create_index(u'goalserve_category', ['name'])

        # Adding index on 'Country', fields ['display_name']
        db.create_index(u'goalserve_country', ['display_name'])

        # Adding index on 'Country', fields ['g_static_id']
        db.create_index(u'goalserve_country', ['g_static_id'])

        # Adding index on 'Country', fields ['g_id']
        db.create_index(u'goalserve_country', ['g_id'])

        # Adding index on 'F1Team', fields ['g_static_id']
        db.create_index(u'goalserve_f1team', ['g_static_id'])

        # Adding index on 'F1Team', fields ['g_id']
        db.create_index(u'goalserve_f1team', ['g_id'])

        # Adding index on 'Player', fields ['name']
        db.create_index(u'goalserve_player', ['name'])

        # Adding index on 'Player', fields ['g_static_id']
        db.create_index(u'goalserve_player', ['g_static_id'])

        # Adding index on 'Player', fields ['g_id']
        db.create_index(u'goalserve_player', ['g_id'])

        # Adding index on 'F1Race', fields ['g_static_id']
        db.create_index(u'goalserve_f1race', ['g_static_id'])

        # Adding index on 'F1Race', fields ['g_id']
        db.create_index(u'goalserve_f1race', ['g_id'])

        # Adding index on 'Team', fields ['display_name']
        db.create_index(u'goalserve_team', ['display_name'])

        # Adding index on 'Team', fields ['name']
        db.create_index(u'goalserve_team', ['name'])

        # Adding index on 'Team', fields ['g_static_id']
        db.create_index(u'goalserve_team', ['g_static_id'])

        # Adding index on 'Team', fields ['g_id']
        db.create_index(u'goalserve_team', ['g_id'])

        # Adding index on 'F1Tournament', fields ['g_static_id']
        db.create_index(u'goalserve_f1tournament', ['g_static_id'])

        # Adding index on 'F1Tournament', fields ['g_id']
        db.create_index(u'goalserve_f1tournament', ['g_id'])


    def backwards(self, orm):
        # Removing index on 'F1Tournament', fields ['g_id']
        db.delete_index(u'goalserve_f1tournament', ['g_id'])

        # Removing index on 'F1Tournament', fields ['g_static_id']
        db.delete_index(u'goalserve_f1tournament', ['g_static_id'])

        # Removing index on 'Team', fields ['g_id']
        db.delete_index(u'goalserve_team', ['g_id'])

        # Removing index on 'Team', fields ['g_static_id']
        db.delete_index(u'goalserve_team', ['g_static_id'])

        # Removing index on 'Team', fields ['name']
        db.delete_index(u'goalserve_team', ['name'])

        # Removing index on 'Team', fields ['display_name']
        db.delete_index(u'goalserve_team', ['display_name'])

        # Removing index on 'F1Race', fields ['g_id']
        db.delete_index(u'goalserve_f1race', ['g_id'])

        # Removing index on 'F1Race', fields ['g_static_id']
        db.delete_index(u'goalserve_f1race', ['g_static_id'])

        # Removing index on 'Player', fields ['g_id']
        db.delete_index(u'goalserve_player', ['g_id'])

        # Removing index on 'Player', fields ['g_static_id']
        db.delete_index(u'goalserve_player', ['g_static_id'])

        # Removing index on 'Player', fields ['name']
        db.delete_index(u'goalserve_player', ['name'])

        # Removing index on 'F1Team', fields ['g_id']
        db.delete_index(u'goalserve_f1team', ['g_id'])

        # Removing index on 'F1Team', fields ['g_static_id']
        db.delete_index(u'goalserve_f1team', ['g_static_id'])

        # Removing index on 'Country', fields ['g_id']
        db.delete_index(u'goalserve_country', ['g_id'])

        # Removing index on 'Country', fields ['g_static_id']
        db.delete_index(u'goalserve_country', ['g_static_id'])

        # Removing index on 'Country', fields ['display_name']
        db.delete_index(u'goalserve_country', ['display_name'])

        # Removing index on 'Category', fields ['name']
        db.delete_index(u'goalserve_category', ['name'])

        # Removing index on 'Category', fields ['g_id']
        db.delete_index(u'goalserve_category', ['g_id'])

        # Removing index on 'Category', fields ['g_static_id']
        db.delete_index(u'goalserve_category', ['g_static_id'])

        # Removing index on 'Category', fields ['display_name']
        db.delete_index(u'goalserve_category', ['display_name'])

        # Removing index on 'Driver', fields ['g_id']
        db.delete_index(u'goalserve_driver', ['g_id'])

        # Removing index on 'Driver', fields ['g_static_id']
        db.delete_index(u'goalserve_driver', ['g_static_id'])

        # Removing index on 'MatchEvent', fields ['event_type']
        db.delete_index(u'goalserve_matchevent', ['event_type'])

        # Removing index on 'MatchEvent', fields ['g_static_id']
        db.delete_index(u'goalserve_matchevent', ['g_static_id'])

        # Removing index on 'MatchEvent', fields ['g_id']
        db.delete_index(u'goalserve_matchevent', ['g_id'])

        # Removing index on 'MatchStandings', fields ['round']
        db.delete_index(u'goalserve_matchstandings', ['round'])

        # Removing index on 'MatchStandings', fields ['g_id']
        db.delete_index(u'goalserve_matchstandings', ['g_id'])

        # Removing index on 'MatchStandings', fields ['g_static_id']
        db.delete_index(u'goalserve_matchstandings', ['g_static_id'])

        # Removing index on 'MatchStandings', fields ['group']
        db.delete_index(u'goalserve_matchstandings', ['group'])

        # Removing index on 'MatchCommentary', fields ['g_id']
        db.delete_index(u'goalserve_matchcommentary', ['g_id'])

        # Removing index on 'MatchCommentary', fields ['g_static_id']
        db.delete_index(u'goalserve_matchcommentary', ['g_static_id'])

        # Removing index on 'Stadium', fields ['name']
        db.delete_index(u'goalserve_stadium', ['name'])

        # Removing index on 'Stadium', fields ['g_id']
        db.delete_index(u'goalserve_stadium', ['g_id'])

        # Removing index on 'Stadium', fields ['g_static_id']
        db.delete_index(u'goalserve_stadium', ['g_static_id'])

        # Removing index on 'F1Commentary', fields ['g_id']
        db.delete_index(u'goalserve_f1commentary', ['g_id'])

        # Removing index on 'F1Commentary', fields ['g_static_id']
        db.delete_index(u'goalserve_f1commentary', ['g_static_id'])

        # Removing index on 'F1Results', fields ['g_id']
        db.delete_index(u'goalserve_f1results', ['g_id'])

        # Removing index on 'F1Results', fields ['g_static_id']
        db.delete_index(u'goalserve_f1results', ['g_static_id'])

        # Removing index on 'Match', fields ['g_id']
        db.delete_index(u'goalserve_match', ['g_id'])

        # Removing index on 'Match', fields ['g_static_id']
        db.delete_index(u'goalserve_match', ['g_static_id'])

        # Removing index on 'Match', fields ['week_number']
        db.delete_index(u'goalserve_match', ['week_number'])

        # Removing index on 'Match', fields ['group_name']
        db.delete_index(u'goalserve_match', ['group_name'])


    models = {
        "%s.%s" % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'goalserve.category': {
            'Meta': {'object_name': 'Category'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.country': {
            'Meta': {'object_name': 'Country'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.driver': {
            'Meta': {'object_name': 'Driver'},
            'birth_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'helmet': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'driver_helmet'", 'null': 'True', 'to': u"orm['images.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'past_teams': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1commentary': {
            'Meta': {'object_name': 'F1Commentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1race': {
            'Meta': {'object_name': 'F1Race'},
            'circuit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Track']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'laps_running': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'race_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'race_type': ('django.db.models.fields.CharField', [], {'default': "'race'", 'max_length': '255'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_laps': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Tournament']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1results': {
            'Meta': {'object_name': 'F1Results'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Driver']"}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_retired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pitstops': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Team']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1team': {
            'Meta': {'object_name': 'F1Team'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'engine': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'launch_date': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'post': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tires': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.f1tournament': {
            'Meta': {'object_name': 'F1Tournament'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.f1track': {
            'Meta': {'object_name': 'F1Track'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'f1track_flag'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_map': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'f1track_map'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['images.Image']"})
        },
        u'goalserve.match': {
            'Meta': {'object_name': 'Match'},
            'attendance_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ht_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_localteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"}),
            'localteam_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'match_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'referee_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'stadium_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'visitorteam': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_visitorteam'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['goalserve.Team']"}),
            'visitorteam_goals': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'week_number': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.matchcommentary': {
            'Meta': {'object_name': 'MatchCommentary'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchevent': {
            'Meta': {'object_name': 'MatchEvent'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'own_goal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'penalty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchlineup': {
            'Meta': {'ordering': "('order',)", 'object_name': 'MatchLineUp'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Player']"}),
            'player_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'player_status': ('django.db.models.fields.CharField', [], {'default': "'player'", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchstandings': {
            'Meta': {'object_name': 'MatchStandings'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'group': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overall_ga': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_gp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_gs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_l': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'overall_w': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'recent_form': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'round': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'timestamp': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_gd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'total_p': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchstats': {
            'Meta': {'object_name': 'MatchStats'},
            'corners': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'fouls': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'offsides': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'possesiontime': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'saves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shots_on_goal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.matchsubstitutions': {
            'Meta': {'object_name': 'MatchSubstitutions'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Match']"}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player_in': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_in'", 'null': 'True', 'to': u"orm['goalserve.Player']"}),
            'player_off': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matchsubstitutions_off'", 'null': 'True', 'to': u"orm['goalserve.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'team_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.player': {
            'Meta': {'object_name': 'Player'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Team']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'goalserve.racedriverposition': {
            'Meta': {'ordering': "('position',)", 'object_name': 'RaceDriverPosition'},
            'driver': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Driver']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.F1Race']"}),
            'table': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'goalserve.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surface': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'goalserve.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'coach': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Country']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'g_bet_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_driver_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            'g_event_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_fix_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_player_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'g_static_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'g_team_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_base': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['images.Image']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['goalserve.Stadium']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'})
        },
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'archive': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'archive_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_example': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'crop_x1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_x2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'crop_y2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fit_in': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'flop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'halign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'images_image_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'smart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.CustomUser']"}),
            'valign': ('django.db.models.fields.CharField', [], {'default': 'False', 'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['goalserve']
