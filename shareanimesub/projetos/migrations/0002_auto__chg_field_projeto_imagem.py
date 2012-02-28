# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Projeto.imagem'
        db.alter_column('projetos_projeto', 'imagem', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))


    def backwards(self, orm):
        
        # Changing field 'Projeto.imagem'
        db.alter_column('projetos_projeto', 'imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    models = {
        'projetos.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'direcao': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'estudio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'fim_exibicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'inicio_exibicao': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_episodios': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projetos']
