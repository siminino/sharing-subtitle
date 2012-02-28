# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Fansub'
        db.create_table('fansubers_fansub', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('fansubers', ['Fansub'])

        # Adding M2M table for field projetos on 'Fansub'
        db.create_table('fansubers_fansub_projetos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fansub', models.ForeignKey(orm['fansubers.fansub'], null=False)),
            ('projeto', models.ForeignKey(orm['projetos.projeto'], null=False))
        ))
        db.create_unique('fansubers_fansub_projetos', ['fansub_id', 'projeto_id'])


    def backwards(self, orm):
        
        # Deleting model 'Fansub'
        db.delete_table('fansubers_fansub')

        # Removing M2M table for field projetos on 'Fansub'
        db.delete_table('fansubers_fansub_projetos')


    models = {
        'fansubers.fansub': {
            'Meta': {'object_name': 'Fansub'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'projetos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projetos.Projeto']", 'symmetrical': 'False'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['fansubers']
