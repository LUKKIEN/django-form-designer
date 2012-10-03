# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'FormDefinitionField.label_sl'
        db.add_column('form_designer_formdefinitionfield', 'label_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_hrv'
        db.add_column('form_designer_formdefinitionfield', 'label_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_de'
        db.add_column('form_designer_formdefinitionfield', 'label_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.label_ro'
        db.add_column('form_designer_formdefinitionfield', 'label_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_sl'
        db.add_column('form_designer_formdefinitionfield', 'initial_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_hrv'
        db.add_column('form_designer_formdefinitionfield', 'initial_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_de'
        db.add_column('form_designer_formdefinitionfield', 'initial_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.initial_ro'
        db.add_column('form_designer_formdefinitionfield', 'initial_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_sl'
        db.add_column('form_designer_formdefinitionfield', 'help_text_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_hrv'
        db.add_column('form_designer_formdefinitionfield', 'help_text_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_de'
        db.add_column('form_designer_formdefinitionfield', 'help_text_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.help_text_ro'
        db.add_column('form_designer_formdefinitionfield', 'help_text_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_sl'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_sl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_hrv'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_hrv', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_de'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_values_ro'
        db.add_column('form_designer_formdefinitionfield', 'choice_values_ro', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_sl'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_sl', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_hrv'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_hrv', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_de'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinitionField.choice_labels_ro'
        db.add_column('form_designer_formdefinitionfield', 'choice_labels_ro', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_sl'
        db.add_column('form_designer_formdefinition', 'title_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_hrv'
        db.add_column('form_designer_formdefinition', 'title_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_de'
        db.add_column('form_designer_formdefinition', 'title_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.title_ro'
        db.add_column('form_designer_formdefinition', 'title_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_sl'
        db.add_column('form_designer_formdefinition', 'mail_to_sl', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_hrv'
        db.add_column('form_designer_formdefinition', 'mail_to_hrv', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_de'
        db.add_column('form_designer_formdefinition', 'mail_to_de', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_to_ro'
        db.add_column('form_designer_formdefinition', 'mail_to_ro', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_sl'
        db.add_column('form_designer_formdefinition', 'mail_subject_sl', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_hrv'
        db.add_column('form_designer_formdefinition', 'mail_subject_hrv', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_de'
        db.add_column('form_designer_formdefinition', 'mail_subject_de', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.mail_subject_ro'
        db.add_column('form_designer_formdefinition', 'mail_subject_ro', self.gf('form_designer.template_field.TemplateCharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_sl'
        db.add_column('form_designer_formdefinition', 'success_message_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_hrv'
        db.add_column('form_designer_formdefinition', 'success_message_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_de'
        db.add_column('form_designer_formdefinition', 'success_message_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.success_message_ro'
        db.add_column('form_designer_formdefinition', 'success_message_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_sl'
        db.add_column('form_designer_formdefinition', 'error_message_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_hrv'
        db.add_column('form_designer_formdefinition', 'error_message_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_de'
        db.add_column('form_designer_formdefinition', 'error_message_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.error_message_ro'
        db.add_column('form_designer_formdefinition', 'error_message_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_sl'
        db.add_column('form_designer_formdefinition', 'submit_label_sl', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_hrv'
        db.add_column('form_designer_formdefinition', 'submit_label_hrv', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_de'
        db.add_column('form_designer_formdefinition', 'submit_label_de', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.submit_label_ro'
        db.add_column('form_designer_formdefinition', 'submit_label_ro', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_sl'
        db.add_column('form_designer_formdefinition', 'message_template_sl', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_hrv'
        db.add_column('form_designer_formdefinition', 'message_template_hrv', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_de'
        db.add_column('form_designer_formdefinition', 'message_template_de', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FormDefinition.message_template_ro'
        db.add_column('form_designer_formdefinition', 'message_template_ro', self.gf('form_designer.template_field.TemplateTextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'FormDefinitionField.label_sl'
        db.delete_column('form_designer_formdefinitionfield', 'label_sl')

        # Deleting field 'FormDefinitionField.label_hrv'
        db.delete_column('form_designer_formdefinitionfield', 'label_hrv')

        # Deleting field 'FormDefinitionField.label_de'
        db.delete_column('form_designer_formdefinitionfield', 'label_de')

        # Deleting field 'FormDefinitionField.label_ro'
        db.delete_column('form_designer_formdefinitionfield', 'label_ro')

        # Deleting field 'FormDefinitionField.initial_sl'
        db.delete_column('form_designer_formdefinitionfield', 'initial_sl')

        # Deleting field 'FormDefinitionField.initial_hrv'
        db.delete_column('form_designer_formdefinitionfield', 'initial_hrv')

        # Deleting field 'FormDefinitionField.initial_de'
        db.delete_column('form_designer_formdefinitionfield', 'initial_de')

        # Deleting field 'FormDefinitionField.initial_ro'
        db.delete_column('form_designer_formdefinitionfield', 'initial_ro')

        # Deleting field 'FormDefinitionField.help_text_sl'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_sl')

        # Deleting field 'FormDefinitionField.help_text_hrv'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_hrv')

        # Deleting field 'FormDefinitionField.help_text_de'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_de')

        # Deleting field 'FormDefinitionField.help_text_ro'
        db.delete_column('form_designer_formdefinitionfield', 'help_text_ro')

        # Deleting field 'FormDefinitionField.choice_values_sl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_sl')

        # Deleting field 'FormDefinitionField.choice_values_hrv'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_hrv')

        # Deleting field 'FormDefinitionField.choice_values_de'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_de')

        # Deleting field 'FormDefinitionField.choice_values_ro'
        db.delete_column('form_designer_formdefinitionfield', 'choice_values_ro')

        # Deleting field 'FormDefinitionField.choice_labels_sl'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_sl')

        # Deleting field 'FormDefinitionField.choice_labels_hrv'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_hrv')

        # Deleting field 'FormDefinitionField.choice_labels_de'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_de')

        # Deleting field 'FormDefinitionField.choice_labels_ro'
        db.delete_column('form_designer_formdefinitionfield', 'choice_labels_ro')

        # Deleting field 'FormDefinition.title_sl'
        db.delete_column('form_designer_formdefinition', 'title_sl')

        # Deleting field 'FormDefinition.title_hrv'
        db.delete_column('form_designer_formdefinition', 'title_hrv')

        # Deleting field 'FormDefinition.title_de'
        db.delete_column('form_designer_formdefinition', 'title_de')

        # Deleting field 'FormDefinition.title_ro'
        db.delete_column('form_designer_formdefinition', 'title_ro')

        # Deleting field 'FormDefinition.mail_to_sl'
        db.delete_column('form_designer_formdefinition', 'mail_to_sl')

        # Deleting field 'FormDefinition.mail_to_hrv'
        db.delete_column('form_designer_formdefinition', 'mail_to_hrv')

        # Deleting field 'FormDefinition.mail_to_de'
        db.delete_column('form_designer_formdefinition', 'mail_to_de')

        # Deleting field 'FormDefinition.mail_to_ro'
        db.delete_column('form_designer_formdefinition', 'mail_to_ro')

        # Deleting field 'FormDefinition.mail_subject_sl'
        db.delete_column('form_designer_formdefinition', 'mail_subject_sl')

        # Deleting field 'FormDefinition.mail_subject_hrv'
        db.delete_column('form_designer_formdefinition', 'mail_subject_hrv')

        # Deleting field 'FormDefinition.mail_subject_de'
        db.delete_column('form_designer_formdefinition', 'mail_subject_de')

        # Deleting field 'FormDefinition.mail_subject_ro'
        db.delete_column('form_designer_formdefinition', 'mail_subject_ro')

        # Deleting field 'FormDefinition.success_message_sl'
        db.delete_column('form_designer_formdefinition', 'success_message_sl')

        # Deleting field 'FormDefinition.success_message_hrv'
        db.delete_column('form_designer_formdefinition', 'success_message_hrv')

        # Deleting field 'FormDefinition.success_message_de'
        db.delete_column('form_designer_formdefinition', 'success_message_de')

        # Deleting field 'FormDefinition.success_message_ro'
        db.delete_column('form_designer_formdefinition', 'success_message_ro')

        # Deleting field 'FormDefinition.error_message_sl'
        db.delete_column('form_designer_formdefinition', 'error_message_sl')

        # Deleting field 'FormDefinition.error_message_hrv'
        db.delete_column('form_designer_formdefinition', 'error_message_hrv')

        # Deleting field 'FormDefinition.error_message_de'
        db.delete_column('form_designer_formdefinition', 'error_message_de')

        # Deleting field 'FormDefinition.error_message_ro'
        db.delete_column('form_designer_formdefinition', 'error_message_ro')

        # Deleting field 'FormDefinition.submit_label_sl'
        db.delete_column('form_designer_formdefinition', 'submit_label_sl')

        # Deleting field 'FormDefinition.submit_label_hrv'
        db.delete_column('form_designer_formdefinition', 'submit_label_hrv')

        # Deleting field 'FormDefinition.submit_label_de'
        db.delete_column('form_designer_formdefinition', 'submit_label_de')

        # Deleting field 'FormDefinition.submit_label_ro'
        db.delete_column('form_designer_formdefinition', 'submit_label_ro')

        # Deleting field 'FormDefinition.message_template_sl'
        db.delete_column('form_designer_formdefinition', 'message_template_sl')

        # Deleting field 'FormDefinition.message_template_hrv'
        db.delete_column('form_designer_formdefinition', 'message_template_hrv')

        # Deleting field 'FormDefinition.message_template_de'
        db.delete_column('form_designer_formdefinition', 'message_template_de')

        # Deleting field 'FormDefinition.message_template_ro'
        db.delete_column('form_designer_formdefinition', 'message_template_ro')


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
            'error_message_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_message_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_template_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mail_from': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_de': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_el': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_es-es': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_fr-fr': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_hrv': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_it-it': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_lv': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_ro': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_subject_sl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_de': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_el': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_en': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_es-es': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_fr-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_fr-fr': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_hrv': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_it-it': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_lv': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-be': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_nl-nl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_ro': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mail_to_sl': ('form_designer.template_field.TemplateCharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'message_template_de': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_el': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_en': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_es-es': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_fr-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_fr-fr': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_hrv': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_it-it': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_lv': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-be': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_nl-nl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_ro': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'message_template_sl': ('form_designer.template_field.TemplateTextField', [], {'null': 'True', 'blank': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "'POST'", 'max_length': '10'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'submit_label_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'submit_label_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_clear': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'success_message_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_message_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'success_redirect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'form_designer.formdefinitionfield': {
            'Meta': {'ordering': "['position']", 'object_name': 'FormDefinitionField'},
            'choice_labels_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_el': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_es-es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_fr-fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_hrv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_it-it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_lv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_ro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_labels_sl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_model': ('form_designer.model_name_field.ModelNameField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_model_empty_label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'choice_values_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_el': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_es-es': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_fr-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_fr-fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_hrv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_it-it': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_lv': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-be': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_nl-nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_ro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'choice_values_sl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'decimal_places': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'field_class': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'help_text_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'help_text_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'include_result': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'initial_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'initial_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_el': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_es-es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_fr-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_fr-fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_hrv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_it-it': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_lv': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl-be': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_nl-nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_ro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'label_sl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'data': ('form_designer.pickled_object_field.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'form_definition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['form_designer.FormDefinition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['form_designer']
