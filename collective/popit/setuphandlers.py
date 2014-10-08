from collective.grok import gs
from collective.popit import MessageFactory as _

@gs.importstep(
    name=u'collective.popit', 
    title=_('collective.popit import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('collective.popit.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
