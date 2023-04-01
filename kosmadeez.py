# DEEZ NUTS

# External Imports
import PySimpleGUI as sg
from time import sleep as Sleep

FILE_TYPES_LIST = [('The correct model','.nuts'), ('no','.dae')]
def GuiMenu():

  # Define the shortcut menubar buttons as strings
  # to shorten the events-related code
  menubar_open    = 'Open              Ctrl-O'
  menubar_clear_q = 'Clear Queue    Ctrl-Q'
  menubar_clear_c = 'Clear Console   Ctrl-R'
  
  # Predefining file_names as empty list 
  # Necessary to make Listbox work
  file_names = list()
  
  # Set the PySimpleGUI Theme
  sg.theme('DarkBlue10')
  
  # Define all UI components
  menubar = [
              [
                '&File', 
                  [
                    f'&{menubar_open}', 
                    f'&{menubar_clear_q}'
                  ]  
              ],
              [
                '&Edit', 
                  [
                    f'&{menubar_clear_c}'
                  ]
              ],
              [
                '&Options', 
                  [
                    '&Modules',
                    '&Restore Files',
                    '&Check for Updates'
                  ]
              ],
              [
                '&Help',
                  [
                    '&About',
                    '&Manual',
                    '&Report a Bug'
                  ]  
              ]
            ]
  frame_import_opts = [
                        [
                          sg.Checkbox('Strip.', visible=True, key='_STRIP-ARMATURE-TREE_',
                                      tooltip='strip.')
                        ],
                        [
                          sg.Combo(['Yes', 'Guacamole'], readonly=False, visible=True)
                        ]
                      ]
  frame_output_type = [
                        [
                          sg.Radio('artikuliert','OUTPUT_TYPE', default=True,
                                    key='_ARTICULATED-MODE_',
                                    tooltip='ARTIKULIEREN SIE IHR WAHRES SELBST'),
                          sg.Radio('Static', 'OUTPUT_TYPE', key='_STATIC-MODE_', 
                                   tooltip='BEWARE OF STATIC ELECTRICITY OTHERWISE YOU MAY BE SUBJECT TO SEVERE CONSEQUENCES'),
                          sg.Radio('Animations\nOnly', 'OUTPUT_TYPE', key='_ANIMATION-MODE_', 
                                   tooltip='Output just the model animations (if they exist)',
                                   visible=False)
                        ]
                      ]

  frame_files_list = [
                        [
                          sg.Listbox(size=(30,10), horizontal_scroll=True, 
                                     values=[], key='_FILES_', enable_events=True, 
                                     tooltip='dont', 
                                     expand_x=True)
                        ]
                     ]

  column_left = [
                  [
                     sg.Image('assets/kozmadeus_moyai.png', subsample=2)
                  ],
                  [
                    sg.Text('Select models to process'), 
                    sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False),
                    sg.FilesBrowse(file_types=FILE_TYPES_LIST, target='_FILEBROWSE_', size=[10,1]),
                  ],
                  [
                    sg.Frame(layout=frame_import_opts, title='Options', expand_x=True)
                  ],
                  [
                    sg.Frame(layout=frame_output_type, title='Output Type', expand_x=True)
                  ],
                  [
                    sg.Button('Submit', expand_x=True), 
                  ],
                  [
                    sg.Frame(layout=frame_files_list, title='Selected Files', expand_x=True)  
                  ]
                ]

  column_right = [
                    [
                      sg.Multiline(expand_x=True, expand_y=True, key='_OUTPUT_', 
                                   auto_refresh=True, write_only=True, autoscroll=True, 
                                   reroute_stdout=True, reroute_stderr=True, 
                                   echo_stdout_stderr=True, disabled=True)
                    ],
                    [
                      sg.Button('Clear Console', pad=((5,200),(0,0))),
                      sg.Text('', text_color='lawn green', key='_STATUS_', size=(5,1)),
                    ]
                 ]

  layout = [
              [
                sg.Menu(menubar),
                sg.Frame(layout = column_left, title=''), 
                sg.Frame(layout = column_right, title='Console', expand_x=True, expand_y=True)
              ]
           ]

  window = sg.Window(f'KOSMADEEZ V1.4', layout, 
                       element_justification='c', finalize=True)
      
  # Define simpler to read shortcut events
  window.bind('<Control-o>', 'Ctrl-O')
  window.bind('<Control-q>', 'Ctrl-Q')
  
  # Connect menubar events with existing ones
  window.bind('<Control-r>', 'Clear Console')
  window.bind('menubar_clear_c', 'Clear Console')
  window.bind('<Return>', 'Submit')
  
  # Bring window to front on start
  window.bring_to_front()

  # Refresh the buttons and locks 
  # when the loop cycle is done
  def RefreshWindowButtons():
    nonlocal window
    nonlocal processing_lock
    window['Submit'].Update(disabled=False)
    window.bind('<Return>', 'Submit')
    processing_lock = False
    window.ding()

  processing_lock = False

  # Main events and values loop
  while True:
    try:

      event, values = window.Read()
      window.refresh()
      
      # Program exit event
      if event is None:
        break


      # Files Queue related events
      elif event == '_FILEBROWSE_':
        file_names = values['_FILEBROWSE_'].split(';')
        window['_FILES_'].Update(file_names)
        
      elif values['_FILES_']:
        file_names.remove(values['_FILES_'][0])
        window['_FILES_'].Update(file_names)
        
        
      # Menubar shortcut related events
      elif event in (menubar_open   , 'Ctrl-O'):
        file_names = sg.PopupGetFile('file to open', no_window=True,
                                     multiple_files=True,
                                     file_types=FILE_TYPES_LIST)
        
        # For some reason, PopupGetFile returns tuple
        # Needs conversion to list
        file_names = list(file_names)
        window['_FILES_'].Update(file_names)
        
      elif event in (menubar_clear_q, 'Ctrl-Q'):
        file_names = []
        window['_FILES_'].Update(file_names)


      # Button related events and others
      elif event in (menubar_clear_c, 'Ctrl-R', 'Clear Console'):
        window['_OUTPUT_'].Update('')

      ### BEGIN SUBMIT
      elif event == 'Submit':
        window['_STATUS_'].Update('')
              
        # Start processing the files
        if file_names:
          
          # Lock the "Submit" button and certain functions
          window['Submit'].Update(disabled=True)
          window.bind('<Return>', 'null')
          processing_lock = True

          print(f'Procesing {file_names}')
          for i in range(1,5):
              print('Extorting monster ransom')
              print('Completing geneva convention tasks against monsters')
              print('Exporting armatures')
              print('RICHARD WHY DID YOU DO IT')
              print('slicing and dicing, remember to season')
              print('Finishing, exporting to file...')
              print('this is insane I cant')
          Sleep(5)
          raise Exception('THANK YOU FOR TRYING OUT THE DEMO, BECOME THE SUBSCRIBER TO COMPLETE THE IMPORTING PROCESS FOR JUST $44/DAY RAWR')

        else:
          print('Please select a file!')
      ### END SUBMIT  

    except Exception as exception:
      window['_STATUS_'].Update('Error!')
      window['_STATUS_'].Update(text_color='red')

      print('Unhandled exception has occured:\n', exception)
      
      RefreshWindowButtons()


if __name__ == '__main__':
  GuiMenu()
