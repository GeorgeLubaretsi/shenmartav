"""
Feed draftlaw
"""
__docformat__ = 'epytext en'

import datetime
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from settings import NUM_FEEDITEMS
from .models import Question



class FeedList (Feed):
    _site = Site.objects.get_current()
    title = _('%s question feed') % _site.name
    description = _('This is a feed of %s questions to representatives.') % _site.name

    def link (self):
        return reverse('question_list')

    def items (self):
        return Question.public.all().order_by('-date')[:NUM_FEEDITEMS]

    def item_pubdate (self, obj):
        return datetime.datetime.combine(obj.date, datetime.time())
