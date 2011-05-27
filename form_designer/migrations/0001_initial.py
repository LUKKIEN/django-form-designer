# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FormDefinition'
        db.create_table('form_designer_formdefinition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, db_index=True)),
            ('title_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('mail_to_nl-nl', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_to_de', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_to_en', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_to_nl-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_to_fr-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_from', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_subject_nl-nl', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_subject_de', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_subject_en', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_subject_nl-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('mail_subject_fr-be', self.gf('form_designer.fields.TemplateCharField')(max_length=255, null=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(default='POST', max_length=10)),
            ('success_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('success_message_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('success_message_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('success_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('success_message_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_message_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_message_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_message_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_message_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('error_message_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submit_label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submit_label_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submit_label_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submit_label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('submit_label_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('log_data', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('success_redirect', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('success_clear', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('allow_get_initial', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('message_template_nl-nl', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True)),
            ('message_template_de', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True)),
            ('message_template_en', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True)),
            ('message_template_nl-be', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True)),
            ('message_template_fr-be', self.gf('form_designer.fields.TemplateTextField')(null=True, blank=True)),
            ('form_template_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('form_designer', ['FormDefinition'])

        # Adding model 'FormLog'
        db.create_table('form_designer_formlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('form_definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form_designer.FormDefinition'])),
            ('data', self.gf('picklefield.fields.PickledObjectField')(null=True, blank=True)),
        ))
        db.send_create_signal('form_designer', ['FormLog'])

        # Adding model 'FormDefinitionField'
        db.create_table('form_designer_formdefinitionfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('form_definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form_designer.FormDefinition'])),
            ('field_class', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=255, db_index=True)),
            ('label_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('label_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('label_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('label_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('label_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('include_result', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('widget', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('initial_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('initial_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('initial_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('initial_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('initial_fr-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('help_text_nl-nl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('help_text_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('help_text_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('help_text_nl-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('help_text_fr-be', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('choice_values_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_values_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_values_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_values_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_values_fr-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_labels_nl-nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_labels_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_labels_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_labels_nl-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('choice_labels_fr-be', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('max_length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('min_length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('min_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max_digits', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('decimal_places', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('regex', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('choice_model', self.gf('form_designer.fields.ModelNameField')(max_length=255, null=True, blank=True)),
            ('choice_model_empty_label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('form_designer', ['FormDefinitionField'])

        # Adding model 'CMSFormDefinition'
        db.create_table('cmsplugin_cmsformdefinition', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('form_definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form_designer.FormDefinition'])),
        ))
        db.send_create_signal('form_designer', ['CMSFormDefinition'])


    def backwards(self, orm):
        
        # Deleting model 'FormDefinition'
        db.delete_table('form_designer_formdefinition')

        # Deleting model 'FormLog'
        db.delete_table('form_designer_formlog')

        # Deleting model 'FormDefinitionField'
        db.delete_table('form_designer_formdefinitionfield')

        # Deleting model 'CMSFormDefinition'
        db.delete_table('cmsplugin_cmsformdefinition')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'form_designer.cmsformdefinition': {
            'Meta': {'object_name': 'CMSFormDefinition', 'db_table': "'cmsplugin_cmsformdefinition'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"})
        },
        'form_designer.formdefinition': {
            'Meta': {'object_name': 'FormDefinition'},
            'action': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allow_get_initial': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'error_message_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_from': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_de': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_en': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_fr-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-nl': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_de': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_en': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_fr-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-be': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-nl': ('form_designer.fields.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'message_template_de': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_en': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_fr-be': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-be': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-nl': ('form_designer.fields.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'submit_label_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'ordering': "['position']", 'object_name': 'FormDefinitionField'},
            'choice_labels_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.fields.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'initial_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'initial_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'label_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'max_digits': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'widget': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formlog': {
            'Meta': {'ordering': "['-created']", 'object_name': 'FormLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['form_designer']
