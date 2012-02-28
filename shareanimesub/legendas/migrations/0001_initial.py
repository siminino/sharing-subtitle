# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Legenda'
        db.create_table('legendas_legenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projetos.Projeto'])),
            ('episodio', self.gf('django.db.models.fields.IntegerField')()),
            ('raws', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fansub', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fansubers.Fansub'], null=True, blank=True)),
        ))
        db.send_create_signal('legendas', ['Legenda'])


    def backwards(self, orm):
        
        # Deleting model 'Legenda'
        db.delete_table('legendas_legenda')


    models = {
        'fansubers.fansub': {
            'Meta': {'object_name': 'Fansub'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'projetos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projetos.Projeto']", 'symmetrical': 'False'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'legendas.legenda': {
            'Meta': {'object_name': 'Legenda'},
            'episodio': ('django.db.models.fields.IntegerField', [], {}),
            'fansub': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fansubers.Fansub']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projetos.Projeto']"}),
            'raws': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'projetos.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'direcao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'estudio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fim_exibicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'inicio_exibicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_episodios': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['legendas']
