# Generated by Django 4.2.16 on 2024-11-19 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('financial_products', '0002_savingproducts_savingoptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1_expected_goal_amount', models.IntegerField()),
                ('q2_goal_duration', models.IntegerField()),
                ('q3_income_source', models.IntegerField()),
                ('q4_emergency_fund_status', models.IntegerField()),
                ('q5_investment_priority', models.IntegerField()),
                ('q6_safety_or_liquidity', models.IntegerField()),
                ('q7_household_status', models.IntegerField()),
                ('q8_average_monthly_income', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SaveInvType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saving_ratio', models.IntegerField()),
                ('inv_ratio', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_products.answers')),
            ],
        ),
        migrations.CreateModel(
            name='PortSaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inst_save_ratio', models.IntegerField()),
                ('reg_save_ratio', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_products.answers')),
            ],
        ),
        migrations.CreateModel(
            name='PortRisk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_ratio', models.IntegerField()),
                ('med_low_ratio', models.IntegerField()),
                ('med_ratio', models.IntegerField()),
                ('med_high_ratio', models.IntegerField()),
                ('high_ratio', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_products.answers')),
            ],
        ),
        migrations.CreateModel(
            name='PortInvType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dom_stock_ratio', models.IntegerField()),
                ('int_stock_ratio', models.IntegerField()),
                ('bond_ratio', models.IntegerField()),
                ('alt_invest_ratio', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_products.answers')),
            ],
        ),
    ]