import sys
import math
from PyQt4 import QtGui

import gui_Album

#class GUI(QtGui.QFrame):
class GUI(QtGui.QMainWindow):
    '''
    /**
     * - der sichtbare Teil der Applikation
     * - 
     */
     getSelectedAlben(self);
    '''
    
    def priv_setNextRowAndColumn(self):
        if(self.aktColumn == self.maxRows):
            self.aktRow = self.aktRow+1
            self.aktColumn = 0;
        else:
            self.aktColumn = self.aktColumn + 1
            
    def priv_arrangeAlben(self):
        ww = 0
        wh = 0
        aw = self.maxWidth
        ah = self.maxHeight
        for albenWidget in self.listOfAlbenWidgets:
            self.priv_setNextRowAndColumn()
            albenWidget.resize(self.maxWidth, self.maxHeight)
            albenWidget.move((self.maxWidth+3)*self.aktColumn, (self.maxHeight+3)*self.aktRow);
            wx = (self.maxWidth+3)*self.aktColumn
            wy = (self.maxHeight+3)*self.aktRow
            
            if(ww < wx+aw):
                ww = wx+aw
            if(wh < wy+ah):
                wh = wy+ah 
        print("width  = %d", (ww))
        print("height = %d", (wh))
        self.scrollWidget.resize(ww, wh)
        
            
    def resizeEvent(self, ev):
        print("def resizeEvent(self, ev):")
#        self.scrollWidget.setGeometry(0,0,ev.size().width(), ev.size().height())
        self.m_scrollArea.setGeometry(0,0,ev.size().width(), ev.size().height())

        #_mainArea->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                         event->size().width(), event->size().height()-SCROLLAREAS_MAIN_Y);
#// BREITE
#  if(event->size().width() > event->oldSize().width())
#  {// Hauptfenster breiter als vorher
#    if(m_scrollWidget->width() > event->size().width())
#    {// Scrollfenster breiter als Hauptfenster
#      // -> alles OK
#    } else if(m_scrollWidget->width() < event->size().width())
#    {// Scrollfenster schmaler als Hauptfenster
#      m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                 event->size().width(), m_scrollWidget->height());
#    }
#  } else if(event->size().width() < event->oldSize().width())
#  {// Hauptfenster schmaler als vorher
#    if(m_scrollWidget->width() > event->size().width())
#    {// Scrollfenster breiter als Hauptfenster
#      if(_maxX_TPW > event->size().width())
#      {// Es gibt TPW's die weiter rechts sind als das Hauptfenster gross ist
#        // --> alles OK
#      } else if(_maxX_TPW < event->size().width())
#      {// Es gibt KEINE TPW's die weiter rechts sind als das Hauptfenster gross ist
#        m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                   event->size().width(), m_scrollWidget->height());
#      }
#    } else if(m_scrollWidget->width() < event->size().width())
#    {// Scrollfenster schmaler als Hauptfenster
#      // theo unmoeglich, da scrollfenster ja vorher auf richtige Groesse gesetzt gewesen sein muss
#      m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                 event->size().width(), m_scrollWidget->height());
#    }
#  }
#  
#  // HOEHE
#  if(event->size().height() > event->oldSize().height())
#  {// Hauptfenster hoeher als vorher
#    if(m_scrollWidget->height() > event->size().height())
#    {// ScrollWidget groesser als das Hauptfenster
#      // --> alles OK
#    }else if(m_scrollWidget->height() < event->size().height())
#    {// ScrollWidget kleiner als das Hauptfenster
#      m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                 m_scrollWidget->width(), event->size().height());
#    }
#  } else if(event->size().height() < event->oldSize().height())
#  {// Hauptfenster weniger hoch als vorher
#    if(m_scrollWidget->height() > event->size().height())
#    {// scrollWidget ist groesser als das Hauptfenster
#      if(_maxY_TPW > event->size().height())
#      {// es gibt noch Objekte 'ausserhalb' des Hauptfensters
#        // --> alles OK
#      } else if(_maxY_TPW < event->size().height())
#      {// es gibt KEINE Objekte 'ausserhalb' des Hauptfensters
#        m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                   m_scrollWidget->width(), event->size().height());
#      }
#    } else if(m_scrollWidget->height() < event->size().height())
#    {// scrollWidget ist kleiner als das Hauptfenster
#      m_scrollWidget->setGeometry(0, SCROLLAREAS_MAIN_Y,
#                                 m_scrollWidget->width(), event->size().height());
#    }
#  }

    
    def __init__(self, mf_listOfAlben, mf_downloadPath, mf_imagePath, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.m_listOfAlben = mf_listOfAlben
        self.m_downloadPath = mf_downloadPath 
        self.m_imagepath = mf_imagePath
                
        self.m_anzahlAlben = self.m_listOfAlben.__len__()
        
        # maximale Anzahl der Zeilen und Spalten ermitteln 
        #  (durch das math.ceil wird sichergestellt,dass immer aufgerundet wird)
        self.maxRows = math.ceil(math.sqrt(self.m_anzahlAlben))
        self.aktColumn = -1;
        self.aktRow = 0;
        self.maxHeight = 0;
        self.maxWidth = 0;
        
        #self.m_main_window = QtGui.QWidget()
        self.m_main_window = self
        self.m_main_window.setWindowTitle('aol-musicLoader')
        #self.scrollWidget = self.m_main_window
        
        self.m_scrollArea = QtGui.QScrollArea(self.m_main_window)
        self.scrollWidget = QtGui.QWidget(self.m_main_window)
        #self.m_scrollArea.setWidget(self.scrollWidget)
        self.m_scrollArea.setWidget(self.scrollWidget)
        self.m_scrollArea.setGeometry(0,0, 800, 600)
        self.m_scrollArea.show()
        self.scrollWidget.setGeometry(0,0, 800, 600)
        self.scrollWidget.show()        
        
        self.m_main_window.show()
        
        self.listOfAlbenWidgets = []
        for album in self.m_listOfAlben:
                self.priv_createWidgets(album)

        self.priv_arrangeAlben()
        



    def priv_createWidgets(self, mf_album):
        albumWidget = gui_Album.AlbumGUI(mf_album.getalbum_thumbnail(), 
                                         self.m_imagepath,
                                         mf_album.getartist_name(), 
                                         mf_album.getalbum_name(), 
                                         mf_album.getdescription(),
                                         #self.m_main_window)
                                         self.scrollWidget)
        self.listOfAlbenWidgets.append(albumWidget)

        if(self.maxWidth < albumWidget.pub_getWidth()):
            self.maxWidth = albumWidget.pub_getWidth()
        if(self.maxHeight < albumWidget.pub_getHeight()):
            self.maxHeight = albumWidget.pub_getHeight()
            


if __name__ == '__main__':
    listOfAlben =[]
    gui = GUI(listOfAlben, "")