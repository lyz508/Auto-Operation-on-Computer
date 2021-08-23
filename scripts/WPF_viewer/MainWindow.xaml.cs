using System.Windows;
using System.Windows.Controls;
using System.IO;
using System.Diagnostics;

namespace autoViewer
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /*Fields*/
        string wanted_scripts = "None";
        string root_directory = "None";
        Process p = new Process();

        public MainWindow ()
        {
            InitializeComponent();

            foreach (string s in File.ReadLines("config.txt"))
            {
                root_directory = s;
            }

            // get files under root directory
            RenewScripts();
        }

        private void RenewScripts()
        {
            this.p.Close();
            ListBox_ListScripts.Items.Clear();
            var files = Directory.EnumerateFiles(root_directory, "auto*.txt");
            foreach (string file in files)
            {
                ListBox_ListScripts.Items.Add(file.Substring(root_directory.Length));
            }
        }

        private void ListBox_ListScripts_SelectionChanged (object sender, SelectionChangedEventArgs e)
        {
            if (ListBox_ListScripts.SelectedItem != null)
            {
                StatusBar_mainStatus.Items.Clear();
                this.wanted_scripts = ListBox_ListScripts.SelectedItem.ToString();
            }
            else
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add("Select again");
            }
        }

        private void BtnReadScript_Click (object sender, RoutedEventArgs e)
        {
            if (this.wanted_scripts == "None")
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add("No selected script.");
            }
            else
            {   // open controller
                string script = this.root_directory + this.wanted_scripts,
                       controller = this.root_directory + "autoController.py", output, error;

                this.p = new Process();

                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.FileName = "python.exe";
                p.StartInfo.Arguments = controller + ' ' + script;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.RedirectStandardOutput = true;

                p.Start();

                output = p.StandardOutput.ReadToEnd();
                error = p.StandardError.ReadToEnd();

                txtBoxShow_Stdout.Text = output;
                txtBlock_Stderr.Text = error;

                p.WaitForExit();
            }
            this.RenewScripts();
        }

        private void BtnClose_Click (object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void Btn_editScript_Click (object sender, RoutedEventArgs e)
        {
            this.p = new Process();

            try
            {
                if (ListBox_ListScripts.SelectedItem == null)
                {   // Doesnt select -> go root directory
                    p.StartInfo.FileName = "explorer.exe";
                    p.StartInfo.Arguments = this.root_directory;
                    p.Start();
                    p.WaitForExit();
                }
                else
                {   // Select -> go selected file
                    p.StartInfo.FileName = "notepad.exe";
                    p.StartInfo.Arguments = this.root_directory + ListBox_ListScripts.SelectedItem.ToString();
                    p.Start();
                    p.WaitForExit();
                }
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add($"{ex.Message}");
            }

            this.RenewScripts();
        }

        private void Btn_Help_Click (object sender, RoutedEventArgs e)
        {
            this.p = new Process();
            try
            {
                p.StartInfo.FileName = "explorer.exe";
                p.StartInfo.Arguments = @"https://github.com/lyz508/Auto-Operation-on-Computer/";
                p.Start();
                p.WaitForExit();
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add($"{ex.Message}");
            }
            this.RenewScripts();
        }

    }
}
